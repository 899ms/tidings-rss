#!/usr/bin/env node
/* Validate candidate feeds through Tidings' production parser. */

const fs = require('node:fs');
const path = require('node:path');

function parseArgs(argv) {
  const values = {};
  for (let i = 2; i < argv.length; i += 2) values[argv[i].replace(/^--/, '')] = argv[i + 1];
  for (const required of ['input', 'output', 'tidings']) {
    if (!values[required]) throw new Error(`missing --${required}`);
  }
  return values;
}

const args = parseArgs(process.argv);
const { parseFeedUrl } = require(path.resolve(args.tidings, 'src/main/feed-service.js'));
const input = JSON.parse(fs.readFileSync(args.input, 'utf8'));
const candidates = input.candidates || input;
const concurrency = Math.max(1, Number(args.concurrency || 8));
const timeoutMs = Math.max(3000, Number(args.timeout || 15000));
const entryLimit = Math.max(5, Math.min(30, Number(args.limit || 15)));
const hostActive = new Map();
const hostWaiters = new Map();
let cursor = 0;
let completed = 0;

function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

async function acquireHost(host) {
  if ((hostActive.get(host) || 0) < 2) {
    hostActive.set(host, (hostActive.get(host) || 0) + 1);
    return;
  }
  await new Promise((resolve) => {
    const queue = hostWaiters.get(host) || [];
    queue.push(resolve);
    hostWaiters.set(host, queue);
  });
  hostActive.set(host, (hostActive.get(host) || 0) + 1);
}

function releaseHost(host) {
  hostActive.set(host, Math.max(0, (hostActive.get(host) || 1) - 1));
  const queue = hostWaiters.get(host) || [];
  const next = queue.shift();
  if (queue.length) hostWaiters.set(host, queue);
  else hostWaiters.delete(host);
  if (next) next();
}

function newestRealDate(entries) {
  const timestamps = entries
    .filter((entry) => !entry.publishedAtInferred && entry.publishedAt)
    .map((entry) => Date.parse(entry.publishedAt))
    .filter(Number.isFinite);
  return timestamps.length ? new Date(Math.max(...timestamps)).toISOString() : null;
}

function realDates(entries) {
  return entries
    .filter((entry) => !entry.publishedAtInferred && entry.publishedAt)
    .map((entry) => Date.parse(entry.publishedAt))
    .filter(Number.isFinite)
    .sort((left, right) => right - left)
    .map((value) => new Date(value).toISOString());
}

function textLengths(entries) {
  return entries.map((entry) => String(entry.text || entry.summary || '').trim().length);
}

function entryTitles(entries) {
  return entries.map((entry) => String(entry.title || '').trim()).filter(Boolean);
}

async function validate(candidate) {
  const started = Date.now();
  const host = new URL(candidate.feed_url).hostname.toLowerCase();
  await acquireHost(host);
  try {
    let lastError;
    for (let attempt = 1; attempt <= 2; attempt += 1) {
      try {
        const feed = await parseFeedUrl(candidate.feed_url, {
          limit: entryLimit,
          timeoutMs,
          fetchIcon: false,
          fetchSubtitles: false
        });
        if (!feed.entries.length) throw new Error('empty feed');
        return {
          feed_url: candidate.feed_url,
          ok: true,
          title: feed.title,
          site_url: feed.htmlUrl,
          item_count: feed.entries.length,
          latest_item_at: newestRealDate(feed.entries),
          item_dates: realDates(feed.entries),
          text_lengths: textLengths(feed.entries),
          entry_titles: entryTitles(feed.entries),
          duration_ms: Date.now() - started
        };
      } catch (error) {
        lastError = error;
        if (attempt === 1 && /429|50[234]|timed? ?out|ECONN|socket/i.test(error.message || '')) {
          await sleep(1200);
          continue;
        }
        break;
      }
    }
    return {
      feed_url: candidate.feed_url,
      ok: false,
      error: String(lastError && lastError.message ? lastError.message : lastError),
      duration_ms: Date.now() - started
    };
  } finally {
    releaseHost(host);
  }
}

async function worker(results) {
  while (cursor < candidates.length) {
    const index = cursor;
    cursor += 1;
    const result = await validate(candidates[index]);
    results[index] = result;
    completed += 1;
    if (completed % 25 === 0 || completed === candidates.length) {
      const passed = results.filter((item) => item && item.ok).length;
      process.stderr.write(`validated ${completed}/${candidates.length} (${passed} passed)\n`);
    }
  }
}

(async () => {
  const results = new Array(candidates.length);
  await Promise.all(Array.from({ length: concurrency }, () => worker(results)));
  const payload = {
    validated_at: args.date || new Date().toISOString().slice(0, 10),
    engine: 'Tidings parseFeedUrl',
    candidate_count: candidates.length,
    passed: results.filter((item) => item.ok).length,
    failed: results.filter((item) => !item.ok).length,
    results
  };
  fs.writeFileSync(args.output, `${JSON.stringify(payload, null, 2)}\n`);
  process.stdout.write(`wrote ${args.output}: ${payload.passed} passed, ${payload.failed} failed\n`);
})().catch((error) => {
  process.stderr.write(`${error.stack || error}\n`);
  process.exitCode = 1;
});
