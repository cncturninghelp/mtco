// mtco_gm_wiring_min.js
// Wires elements labeled exactly "G/M code trainer". No renaming, no once:true.
export default function wireGM(opts = {}){
  const trainerHref = opts.href || 'gm_code_trainer.html';
  const norm = s => (s||'').replace(/\s+/g,' ').trim().toLowerCase();

  function markTargets(){
    const hero = document.querySelector('.hero-visual');
    if (!hero) return;
    // The card in the hero grid
    const cards = hero.querySelectorAll('.grid .card');
    for (const card of cards){
      const h3 = card.querySelector('h3');
      if (!h3) continue;
      if (norm(h3.textContent) === 'g/m code trainer'){
        card.dataset.gmOpen = '1';
        card.setAttribute('role','link');
        card.style.cursor = 'pointer';
        if (!card.hasAttribute('tabindex')) card.setAttribute('tabindex','0');
      }
    }
    // Any other explicit button/label
    const nodes = document.querySelectorAll('a,button,[role="button"],.btn,h3,h4,.chip');
    for (const el of nodes){
      if (norm(el.textContent) === 'g/m code trainer'){
        el.dataset.gmOpen = '1';
        if (!el.hasAttribute('tabindex')) el.setAttribute('tabindex','0');
        el.style.cursor = 'pointer';
        if (!el.hasAttribute('role')) el.setAttribute('role','link');
      }
    }
  }

  function handleNav(target){
    const trigger = target.closest('[data-gm-open="1"]');
    if (trigger){
      window.location.href = trainerHref;
      return true;
    }
    return false;
  }

  document.addEventListener('click', (e) => {
    if (handleNav(e.target)) e.preventDefault();
  });
  document.addEventListener('keydown', (e) => {
    if ((e.key === 'Enter' || e.key === ' ') && handleNav(e.target)) e.preventDefault();
  });

  function init(){
    markTargets();
    requestAnimationFrame(markTargets);
    setTimeout(markTargets, 50);
  }

  if (document.readyState === 'complete' || document.readyState === 'interactive') {
    setTimeout(init, 0);
  } else {
    document.addEventListener('DOMContentLoaded', init);
  }

  // Keep it resilient
  const host = document.querySelector('.hero-visual') || document.body;
  if (host && 'MutationObserver' in window){
    const mo = new MutationObserver(() => markTargets());
    mo.observe(host, { childList:true, subtree:true });
  }
}
