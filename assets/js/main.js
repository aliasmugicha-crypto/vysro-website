const menuButton = document.querySelector('[data-menu-button]');
const menu = document.querySelector('[data-menu]');

if (menuButton && menu) {
  const desktop = window.matchMedia('(min-width: 1020px)');

  const syncMenu = () => {
    if (desktop.matches) {
      menu.hidden = false;
      menuButton.setAttribute('aria-expanded', 'true');
    } else {
      menu.hidden = true;
      menuButton.setAttribute('aria-expanded', 'false');
    }
  };

  menuButton.addEventListener('click', () => {
    const expanded = menuButton.getAttribute('aria-expanded') === 'true';
    menuButton.setAttribute('aria-expanded', String(!expanded));
    menu.hidden = expanded;
  });

  desktop.addEventListener('change', syncMenu);
  syncMenu();
}

// Brand mark and website descriptor are deliberately separated. The mark can remain
// stable while positioning language evolves with the business.
document.querySelectorAll('.brand').forEach((brand) => {
  brand.innerHTML = '<img src="assets/logo/vysro-logo.webp" alt="VYSRO" style="display:block;width:min(11.5rem,42vw);height:auto">';
});

const heroLogo = document.querySelector('.logo-placeholder');
if (heroLogo) {
  heroLogo.innerHTML = '<img src="assets/logo/vysro-logo.webp" alt="VYSRO — Operational Intelligence Systems" style="display:block;width:min(22rem,82vw);height:auto;margin:auto">';
  heroLogo.style.background = '#fff';
  heroLogo.style.border = '0';
  heroLogo.style.minHeight = '0';
}
