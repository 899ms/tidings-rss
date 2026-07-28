#!/usr/bin/env node
/* Capture a real Tidings import in an isolated test profile. */

const fs = require('node:fs');
const os = require('node:os');
const path = require('node:path');

function parseArgs(argv) {
  const split = argv.indexOf('--');
  const optionArgs = split === -1 ? argv : argv.slice(0, split);
  const opmlArgs = split === -1 ? [] : argv.slice(split + 1);
  const options = {};
  for (let index = 2; index < optionArgs.length; index += 2) {
    options[optionArgs[index].replace(/^--/, '')] = optionArgs[index + 1];
  }
  for (const name of ['tidings', 'output', 'report']) {
    if (!options[name]) throw new Error(`missing --${name}`);
  }
  if (!opmlArgs.length) throw new Error('provide at least one OPML path after --');
  return { options, opmlPaths: opmlArgs.map((value) => path.resolve(value)) };
}

const { options, opmlPaths } = parseArgs(process.argv);
const tidingsRoot = path.resolve(options.tidings);
const { _electron: electron } = require(path.join(tidingsRoot, 'node_modules/@playwright/test'));
const { JsonStore } = require(path.join(tidingsRoot, 'src/main/store'));
const dataDir = fs.mkdtempSync(path.join(os.tmpdir(), 'tidings-rss-preview-'));

const PREFERRED_FEEDS = [
  'The latest research from Google',
  'Amazon Science',
  'MIT News - Artificial intelligence',
  'Quanta Magazine',
  'NASA',
  'Ars Technica - All content',
  'MIT Technology Review',
  'The Verge — News',
  'TechCrunch',
  'WIRED'
];

function bodyText(detail = {}) {
  return (detail.body || [])
    .map((block) => block.zh || block.en || block.html || '')
    .join(' ')
    .replace(/<[^>]+>/g, ' ')
    .replace(/\s+/g, ' ')
    .trim();
}

function imageBlocks(detail = {}) {
  return (detail.body || []).filter((block) => block.t === 'img' && /^https?:\/\//i.test(block.src || ''));
}

function contentQuality(detail = {}) {
  const text = bodyText(detail);
  const boilerplate = [
    /\blog out\b/i,
    /\bchange password\b/i,
    /\bsaved articles\b/i,
    /create a reading list by clicking/i,
    /\bsign in to continue\b/i
  ].filter((pattern) => pattern.test(text)).map((pattern) => pattern.source);
  const substantialParagraphs = (detail.body || []).filter((block) => {
    if (!['p', 'quote', 'html', 'list'].includes(block.t)) return false;
    const value = String(block.zh || block.en || block.html || '').replace(/<[^>]+>/g, ' ').replace(/\s+/g, ' ').trim();
    return value.length >= 80;
  }).length;
  return { textLength: text.length, substantialParagraphs, boilerplate };
}

function isQualifiedCandidate(item) {
  return item.detail?.fullTextStatus === 'full'
    && item.imageCount > 0
    && item.textLength >= 600
    && item.substantialParagraphs >= 3
    && item.boilerplate.length === 0;
}

async function importAndVerify(page, opmlPath) {
  const result = await page.evaluate((filePath) => window.tidings.importOpmlPath(filePath), opmlPath);
  const finalByFeed = new Map(result.results.map((item) => [item.feedId, item]));
  let retryPassed = 0;
  for (let attempt = 1; attempt <= 3; attempt += 1) {
    const failedIds = [...finalByFeed.values()].filter((item) => !item.ok).map((item) => item.feedId);
    if (!failedIds.length) break;
    await page.waitForTimeout(800 * attempt);
    const retries = await page.evaluate(
      (feedIds) => Promise.all(feedIds.map((feedId) => window.tidings.refreshFeed(feedId))),
      failedIds
    );
    retries.forEach((item) => {
      if (item.ok && !finalByFeed.get(item.feedId)?.ok) retryPassed += 1;
      finalByFeed.set(item.feedId, item);
    });
  }
  const finalResults = [...finalByFeed.values()];
  return {
    file: path.basename(opmlPath),
    imported: result.imported,
    invalid: result.invalid,
    limit_skipped: result.limitSkipped,
    initial_refresh_passed: result.results.filter((item) => item.ok).length,
    retry_passed: retryPassed,
    final_refresh_passed: finalResults.filter((item) => item.ok).length,
    final_refresh_failed: finalResults.filter((item) => !item.ok).length,
    failed_feed_ids: finalResults.filter((item) => !item.ok).map((item) => item.feedId)
  };
}

async function candidateEntries(page, snapshot) {
  const feedsByTitle = new Map(snapshot.feedsRaw.map((feed) => [feed.title, feed]));
  const preferred = PREFERRED_FEEDS.map((title) => feedsByTitle.get(title)).filter(Boolean);
  const fallback = snapshot.feedsRaw
    .filter((feed) => !preferred.some((item) => item.id === feed.id) && feed.type === 'articles')
    .sort((left, right) => Number(!!right.iconUrl) - Number(!!left.iconUrl));
  const feeds = [...preferred, ...fallback].slice(0, 14);
  const candidates = [];
  const seen = new Set();
  for (const feed of feeds) {
    const result = await page.evaluate(
      ({ feedId }) => window.tidings.queryEntries({ view: 'articles', feedIds: [feedId], limit: 3 }),
      { feedId: feed.id }
    );
    for (const item of result.items || []) {
      if (seen.has(item.id)) continue;
      seen.add(item.id);
      candidates.push({ ...item, feedId: feed.id, feedTitle: feed.title });
    }
  }
  return candidates;
}

async function enrichCandidates(page, candidates) {
  const enriched = [];
  for (let index = 0; index < candidates.length; index += 3) {
    const batch = candidates.slice(index, index + 3);
    const results = await Promise.all(batch.map(async (candidate) => {
      try {
        await page.evaluate(
          ({ entryId }) => window.tidings.enrichEntry(entryId, { force: true, timeoutMs: 25000, attachments: false }),
          { entryId: candidate.id }
        );
        const detail = await page.evaluate((entryId) => window.tidings.getEntryDetail(entryId), candidate.id);
        const images = imageBlocks(detail);
        const firstImageIndex = (detail.body || []).findIndex((block) => block.t === 'img' && /^https?:\/\//i.test(block.src || ''));
        const quality = contentQuality(detail);
        return {
          ...candidate,
          detail,
          imageCount: images.length,
          firstImageIndex,
          ...quality
        };
      } catch (error) {
        return { ...candidate, error: error.message || String(error) };
      }
    }));
    enriched.push(...results);
    const qualified = enriched.filter(isQualifiedCandidate);
    if (qualified.length >= 4 && new Set(qualified.map((item) => item.feedTitle)).size >= 2) break;
  }
  return enriched
    .filter(isQualifiedCandidate)
    .sort((left, right) => {
      const leftIndex = PREFERRED_FEEDS.indexOf(left.feedTitle);
      const rightIndex = PREFERRED_FEEDS.indexOf(right.feedTitle);
      const leftPreferred = leftIndex < 0 ? 0 : PREFERRED_FEEDS.length - leftIndex;
      const rightPreferred = rightIndex < 0 ? 0 : PREFERRED_FEEDS.length - rightIndex;
      const leftScore = leftPreferred * 20 + left.imageCount * 8 - Math.max(0, left.firstImageIndex) * 4 + Math.min(30, left.textLength / 200);
      const rightScore = rightPreferred * 20 + right.imageCount * 8 - Math.max(0, right.firstImageIndex) * 4 + Math.min(30, right.textLength / 200);
      return rightScore - leftScore;
    });
}

async function activateCandidate(page, candidate, diagnostics) {
  const feed = page.locator(`.feed-item[data-feed-id="${candidate.feedId}"]`);
  if (!await feed.count()) {
    diagnostics.push({ id: candidate.id, title: candidate.title, source: candidate.feedTitle, reason: 'feed_not_rendered' });
    return null;
  }
  await feed.click();
  const row = page.locator(`#listBody .art-item[data-entry-id="${candidate.id}"]`);
  try {
    await row.waitFor({ state: 'visible', timeout: 10000 });
    await row.click();
    await page.waitForFunction(
      ({ entryId }) => document.querySelector('.art-item.active')?.dataset.entryId === entryId
        && !!document.querySelector('#contentTitle')?.textContent.trim(),
      { entryId: candidate.id },
      { timeout: 10000 }
    );
    await page.locator('#contentBody .content-note.ok').waitFor({ state: 'visible', timeout: 15000 });
    const firstImage = page.locator('#contentBody .article-image-frame').first();
    await firstImage.waitFor({ state: 'attached', timeout: 15000 });
    await firstImage.scrollIntoViewIfNeeded();
    await firstImage.waitFor({ state: 'visible', timeout: 5000 });
    await page.waitForFunction(
      () => document.querySelector('#contentBody .article-image-frame')?.classList.contains('is-loaded'),
      null,
      { timeout: 20000 }
    );
    await page.locator('#contentBody').evaluate((node) => {
      node.scrollTop = 0;
      node.dispatchEvent(new Event('scroll'));
    });
    await page.waitForTimeout(500);
    const ui = await page.evaluate(() => {
      const body = document.querySelector('#contentBody');
      const title = document.querySelector('#contentTitle');
      const firstFrame = body?.querySelector('.article-image-frame.is-loaded');
      const frameRect = firstFrame?.getBoundingClientRect();
      const titleRect = title?.getBoundingClientRect();
      return {
        active_entry_id: document.querySelector('.art-item.active')?.dataset.entryId || '',
        title: title?.textContent.trim() || '',
        full_text_ready: !!body?.querySelector('.content-note.ok'),
        fetching_full_text_visible: /Fetching full text|正在抓取全文/i.test(body?.textContent || ''),
        full_text_error_visible: !!body?.querySelector('.content-note.warn'),
        reader_boilerplate_visible: /\bLog out\b|\bChange password\b|\bSaved Articles\b|create a reading list by clicking/i.test(body?.textContent || ''),
        loaded_article_images: body?.querySelectorAll('.article-image-frame.is-loaded').length || 0,
        failed_article_images: body?.querySelectorAll('.article-image-frame.is-error').length || 0,
        first_image_visible: !!frameRect && frameRect.top < window.innerHeight - 30 && frameRect.bottom > 0,
        title_visible: !!titleRect && titleRect.top >= 0 && titleRect.bottom < window.innerHeight
      };
    });
    if (!ui.full_text_ready
      || ui.fetching_full_text_visible
      || ui.full_text_error_visible
      || ui.reader_boilerplate_visible
      || ui.loaded_article_images < 1
      || ui.failed_article_images > 0
      || !ui.first_image_visible
      || !ui.title_visible) {
      diagnostics.push({ id: candidate.id, title: candidate.title, source: candidate.feedTitle, reason: 'ui_assertion_failed', ui });
      return null;
    }
    return ui;
  } catch (error) {
    diagnostics.push({ id: candidate.id, title: candidate.title, source: candidate.feedTitle, reason: error.message || String(error) });
    return null;
  }
}

async function waitForVisibleThumbnails(page) {
  try {
    await page.waitForFunction(() => {
      const images = [...document.querySelectorAll('#listBody .art-thumb')];
      return images.every((img) => img.hidden || (img.complete && img.naturalWidth > 0));
    }, null, { timeout: 30000 });
  } catch {}
  return page.evaluate(() => ({
    loaded: [...document.querySelectorAll('#listBody .art-thumb')]
      .filter((img) => !img.hidden && img.complete && img.naturalWidth > 0).length,
    hidden_or_failed: [...document.querySelectorAll('#listBody .art-thumb')]
      .filter((img) => img.hidden || !img.naturalWidth).length
  }));
}

async function main() {
  const store = new JsonStore(dataDir, { initialLocale: 'en-US' });
  store.load();
  store.updateEntitlement({
    plan: 'pro_lifetime',
    source: 'development',
    lastCheckedAt: new Date().toISOString()
  });

  const app = await electron.launch({
    args: [tidingsRoot],
    cwd: tidingsRoot,
    env: {
      ...process.env,
      TIDINGS_DATA_DIR: dataDir,
      TIDINGS_DISABLE_AUTO_REFRESH: '1',
      TIDINGS_ENABLE_TEST_API: '1',
      TIDINGS_UI_LOCALE: 'en-US'
    }
  });
  try {
    const page = await app.firstWindow();
    await app.evaluate(({ BrowserWindow }) => {
      const window = BrowserWindow.getAllWindows()[0];
      window.setBounds({ x: 80, y: 60, width: 1440, height: 900 });
    });
    await page.locator('#app').waitFor({ state: 'visible' });
    const imports = [];
    for (const opmlPath of opmlPaths) imports.push(await importAndVerify(page, opmlPath));
    if (imports.some((item) => item.final_refresh_failed > 0)) {
      throw new Error(`refusing to capture with failed feeds: ${JSON.stringify(imports)}`);
    }
    await page.reload({ waitUntil: 'domcontentloaded' });
    await page.locator('#app').waitFor({ state: 'visible' });
    const snapshot = await page.evaluate(() => window.tidings.getSnapshot());
    const candidates = await enrichCandidates(page, await candidateEntries(page, snapshot));
    let selected = null;
    let uiVerification = null;
    const candidateDiagnostics = [];
    for (const candidate of candidates) {
      const verified = await activateCandidate(page, candidate, candidateDiagnostics);
      if (!verified) continue;
      selected = candidate;
      uiVerification = verified;
      break;
    }
    if (!selected) {
      const enriched = candidates.map((item) => ({
        id: item.id,
        title: item.title,
        source: item.feedTitle,
        status: item.detail?.fullTextStatus,
        image_blocks: item.imageCount,
        first_image_index: item.firstImageIndex,
        text_characters: item.textLength,
        substantial_paragraphs: item.substantialParagraphs,
        boilerplate: item.boilerplate
      }));
      throw new Error(`no image-rich article completed full-text and UI verification: ${JSON.stringify({ enriched, candidateDiagnostics })}`);
    }
    const thumbnailVerification = await waitForVisibleThumbnails(page);
    fs.mkdirSync(path.dirname(path.resolve(options.output)), { recursive: true });
    await page.screenshot({ path: path.resolve(options.output), type: 'png' });
    const finalSnapshot = await page.evaluate(() => window.tidings.getSnapshot());
    const failedIds = new Set(imports.flatMap((item) => item.failed_feed_ids));
    const failedFeeds = finalSnapshot.feedsRaw
      .filter((feed) => failedIds.has(feed.id))
      .map((feed) => ({ title: feed.title, feed_url: feed.xmlUrl, error: feed.error }));
    const visibleArticles = Object.values(finalSnapshot.articles || {})
      .reduce((total, section) => total + (section.items?.length || 0), 0);
    const report = {
      captured_at: new Date().toISOString(),
      app: 'Tidings',
      isolated_profile: true,
      screenshot: options.output,
      imports,
      unique_feeds: finalSnapshot.feedsRaw?.length || 0,
      categories: finalSnapshot.categories?.length || 0,
      visible_articles: visibleArticles,
      failed_feeds: failedFeeds,
      selected_article: {
        id: selected.id,
        title: selected.title,
        source: selected.feedTitle,
        full_text_status: selected.detail.fullTextStatus,
        body_blocks: selected.detail.body?.length || 0,
        image_blocks: selected.imageCount,
        text_characters: selected.textLength,
        substantial_paragraphs: selected.substantialParagraphs
      },
      ui_verification: uiVerification,
      thumbnail_verification: thumbnailVerification
    };
    fs.mkdirSync(path.dirname(path.resolve(options.report)), { recursive: true });
    fs.writeFileSync(path.resolve(options.report), `${JSON.stringify(report, null, 2)}\n`);
    process.stdout.write(`${JSON.stringify(report, null, 2)}\n`);
  } finally {
    await app.close();
  }
}

main()
  .finally(() => fs.rmSync(dataDir, { recursive: true, force: true }))
  .catch((error) => {
    process.stderr.write(`${error.stack || error}\n`);
    process.exitCode = 1;
  });
