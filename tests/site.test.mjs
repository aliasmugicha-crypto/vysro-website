import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';

const root = path.resolve(import.meta.dirname, '..');
const requiredFiles = [
  'index.html',
  'systems.html',
  'services.html',
  'industries.html',
  'standards.html',
  'about.html',
  'assets/styles.css',
  'assets/app.js',
  'assets/vysro-logo.svg',
  'netlify.toml'
];

const pages = ['index.html', 'systems.html', 'services.html', 'industries.html', 'standards.html', 'about.html'];

function read(rel) {
  return fs.readFileSync(path.join(root, rel), 'utf8');
}

test('all deployable website files exist', () => {
  for (const rel of requiredFiles) {
    assert.equal(fs.existsSync(path.join(root, rel)), true, `missing ${rel}`);
  }
});

test('homepage contains the approved brand positioning and technical-business focus', () => {
  const html = read('index.html');
  assert.match(html, /Turning Operational Knowledge into Intelligent Systems\./);
  assert.match(html, /Operational[^<]*•[^<]*Intelligence[^<]*•[^<]*Systems/);
  assert.match(html, /Ready-Mix/i);
  assert.match(html, /small and medium|SME/i);
  assert.match(html, /manufacturing/i);
  assert.match(html, /construction/i);
});

test('public pages do not mention prohibited client/company names', () => {
  for (const page of pages) {
    const html = read(page);
    assert.doesNotMatch(html, /TEMACO/i, `${page} contains TEMACO`);
  }
});

test('every page links to the complete corporate navigation', () => {
  const targets = ['index.html', 'systems.html', 'services.html', 'industries.html', 'standards.html', 'about.html'];
  for (const page of pages) {
    const html = read(page);
    for (const target of targets) {
      assert.match(html, new RegExp(`href=["']${target.replace('.', '\\.')}`), `${page} missing ${target}`);
    }
  }
});

test('Netlify publishes the repository root with no build command requirement', () => {
  const toml = read('netlify.toml');
  assert.match(toml, /publish\s*=\s*["']\.["']/);
  assert.doesNotMatch(toml, /^\s*command\s*=/m);
});
