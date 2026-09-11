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
