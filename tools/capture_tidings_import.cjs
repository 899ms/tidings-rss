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
    for (const opmlPath of opmlPaths) {
      const result = await page.evaluate((filePath) => window.tidings.importOpmlPath(filePath), opmlPath);
      const failed = result.results.filter((item) => !item.ok);
      let retryResults = [];
      if (failed.length) {
        await page.waitForTimeout(1200);
        retryResults = await page.evaluate(
          (feedIds) => Promise.all(feedIds.map((feedId) => window.tidings.refreshFeed(feedId))),
          failed.map((item) => item.feedId)
        );
      }
      const retryByFeed = new Map(retryResults.map((item) => [item.feedId, item]));
      const finalResults = result.results.map((item) => retryByFeed.get(item.feedId) || item);
      imports.push({
        file: path.basename(opmlPath),
        imported: result.imported,
        invalid: result.invalid,
        limit_skipped: result.limitSkipped,
        initial_refresh_passed: result.results.filter((item) => item.ok).length,
        retry_passed: retryResults.filter((item) => item.ok).length,
        final_refresh_passed: finalResults.filter((item) => item.ok).length,
        final_refresh_failed: finalResults.filter((item) => !item.ok).length,
        failed_feed_ids: finalResults.filter((item) => !item.ok).map((item) => item.feedId)
      });
    }
    await page.reload({ waitUntil: 'domcontentloaded' });
    await page.locator('#app').waitFor({ state: 'visible' });
    const news = page.locator('.feed-group-select', { hasText: 'News' }).first();
    if (await news.count()) await news.click();
    await page.locator('#listBody .art-item').first().waitFor({ state: 'visible', timeout: 30000 });
    fs.mkdirSync(path.dirname(path.resolve(options.output)), { recursive: true });
    await page.screenshot({ path: path.resolve(options.output), type: 'png' });
    const snapshot = await page.evaluate(() => window.tidings.getSnapshot());
    const failedIds = new Set(imports.flatMap((item) => item.failed_feed_ids));
    const failedFeeds = snapshot.feedsRaw
      .filter((feed) => failedIds.has(feed.id))
      .map((feed) => ({ title: feed.title, feed_url: feed.xmlUrl, error: feed.error }));
    const visibleArticles = Object.values(snapshot.articles || {})
      .reduce((total, section) => total + (section.items?.length || 0), 0);
    const report = {
      captured_at: new Date().toISOString(),
      app: 'Tidings',
      isolated_profile: true,
      screenshot: options.output,
      imports,
      unique_feeds: snapshot.feedsRaw?.length || 0,
      categories: snapshot.categories?.length || 0,
      visible_articles: visibleArticles,
      failed_feeds: failedFeeds
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
