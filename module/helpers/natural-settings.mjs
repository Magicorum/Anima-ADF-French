/**
 * Gestionnaire des paramètres naturels pour les compétences secondaires
 * Ce script gère l'ouverture/fermeture des sous-menus pour les bonus naturels
 */

export class NaturalSettingsManager {
  constructor() {
    this.activeSubmenu = null;
    this.init();
  }

  init() {
    // Déléguer les événements sur le document pour les boutons d'engrenage
    document.addEventListener('click', (event) => {
      if (event.target.classList.contains('skill-natural-toggle')) {
        this.handleToggleClick(event);
      }
    });

    // Fermer les sous-menus quand on clique ailleurs
    document.addEventListener('click', (event) => {
      if (!event.target.closest('.skill-natural-toggle') && !event.target.closest('.skill-natural-submenu')) {
        this.closeAllSubmenus();
      }
    });
  }

  handleToggleClick(event) {
    event.preventDefault();
    event.stopPropagation();

    const button = event.target;
    const skill = button.dataset.skill;
    const category = button.dataset.category;

    // Créer l'ID du sous-menu
    const submenuId = `natural-submenu-${category}-${skill}`;
    const submenu = document.getElementById(submenuId);

    if (!submenu) {
      console.warn(`Sous-menu non trouvé: ${submenuId}`);
      return;
    }

    // Fermer le sous-menu actif s'il y en a un d'ouvert
    if (this.activeSubmenu && this.activeSubmenu !== submenu) {
      this.closeSubmenu(this.activeSubmenu);
    }

    // Basculer l'état du sous-menu cliqué
    if (submenu.style.display === 'none' || submenu.style.display === '') {
      this.openSubmenu(submenu);
    } else {
      this.closeSubmenu(submenu);
    }
  }

  openSubmenu(submenu) {
    submenu.style.display = 'block';
    this.activeSubmenu = submenu;

    // Animation d'ouverture
    submenu.style.opacity = '0';
    submenu.style.transform = 'translateY(-10px)';

    requestAnimationFrame(() => {
      submenu.style.transition = 'all 0.2s ease';
      submenu.style.opacity = '1';
      submenu.style.transform = 'translateY(0)';
    });
  }

  closeSubmenu(submenu) {
    submenu.style.opacity = '0';
    submenu.style.transform = 'translateY(-10px)';

    setTimeout(() => {
      submenu.style.display = 'none';
      if (this.activeSubmenu === submenu) {
        this.activeSubmenu = null;
      }
    }, 200);
  }

  closeAllSubmenus() {
    if (this.activeSubmenu) {
      this.closeSubmenu(this.activeSubmenu);
    }

    // Fermer tous les sous-menus visibles
    const submenus = document.querySelectorAll('.skill-natural-submenu[style*="display: block"]');
    submenus.forEach(submenu => {
      this.closeSubmenu(submenu);
    });
  }
}

// Initialiser le gestionnaire quand le DOM est chargé
document.addEventListener('DOMContentLoaded', () => {
  window.naturalSettingsManager = new NaturalSettingsManager();
});

// Exporter pour Foundry VTT
export default NaturalSettingsManager;
