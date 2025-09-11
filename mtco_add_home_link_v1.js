
// mtco_add_home_link_v1.js
(function () {
  function computeHomeHref() {
    try {
      // If hosted on GitHub Pages under /mtco/, go to that root. Otherwise fall back to index.html
      if (location.hostname.endsWith('github.io') && location.pathname.includes('/mtco/')) return '/mtco/';
      // If opened from file:// or local dev, look for a sibling index.html
      return 'index.html';
    } catch (e) {
      return 'index.html';
    }
  }

  function ensureChipStyles() {
    // If site already has .chip styles, skip adding ours
    var needs = !document.querySelector('style[data-mtco-home-chip]');
    if (!needs) return;
    var s = document.createElement('style');
    s.setAttribute('data-mtco-home-chip', 'true');
    s.textContent = [
      '.mtco-home-fab{position:fixed;right:14px;bottom:14px;padding:10px 14px;border-radius:999px;',
      'background:var(--accent, #ff7a1a);color:#1b0f07;border:1px solid rgba(0,0,0,.2);',
      'font-weight:700;z-index:9999;box-shadow:0 6px 20px rgba(0,0,0,.25)}',
      '@media (min-width:961px){.mtco-home-fab{display:none}}'
    ].join('');
    document.head.appendChild(s);
  }

  function addHomeChip(nav, href) {
    try {
      var chip = document.createElement('a');
      chip.id = 'mtcoHomeChip';
      chip.href = href;
      chip.textContent = 'Home';
      // Prefer site chip styles if present
      chip.className = (document.querySelector('.chip')) ? 'chip' : '';
      // If no chip style, add some minimal padding so it doesn't look broken
      if (!chip.className) { chip.style.cssText = 'padding:8px 12px;border-radius:12px;border:1px solid rgba(255,255,255,.08);display:inline-block;margin-right:8px'; }
      nav.insertBefore(chip, nav.firstChild);
    } catch (e) {}
  }

  function makeBrandClickable(header, href) {
    try {
      var brand = header.querySelector('.brand,[class*="brand"], .site-title, h1, .title');
      if (!brand) return;
      // If already wrapped in a link, update href instead
      var parentLink = brand.closest('a');
      if (parentLink) { parentLink.href = href; parentLink.title = 'MTCO Home'; return; }
      // Otherwise wrap in anchor
      var a = document.createElement('a');
      a.href = href;
      a.id = 'mtcoHomeLink';
      a.title = 'MTCO Home';
      a.style.textDecoration = 'none';
      brand.parentNode.insertBefore(a, brand);
      a.appendChild(brand);
      a.style.cursor = 'pointer';
    } catch (e) {}
  }

  function addMobileFab(href) {
    try {
      ensureChipStyles();
      var fab = document.createElement('a');
      fab.href = href;
      fab.textContent = 'Home';
      fab.className = 'mtco-home-fab';
      fab.setAttribute('aria-label', 'Go to MTCO Home');
      document.body.appendChild(fab);
    } catch (e) {}
  }

  function run() {
    var href = computeHomeHref();
    var header = document.querySelector('header') || document.querySelector('[data-role="header"]');
    var nav = header ? header.querySelector('nav') : document.querySelector('nav');

    if (nav) addHomeChip(nav, href);
    if (header) makeBrandClickable(header, href);
    // Add mobile FAB as a fallback if nav is hidden by CSS
    addMobileFab(href);
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', run);
  else run();
})();
