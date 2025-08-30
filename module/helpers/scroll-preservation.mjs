/**
 * Scroll Preservation Manager
 * Prevents unwanted scrolling when form inputs are updated
 */
export class ScrollPreservationManager {
  constructor() {
    this.scrollPosition = 0;
    this.initializeEventListeners();
  }

  /**
   * Initialize event listeners for scroll preservation
   */
  initializeEventListeners() {
    // Preserve scroll position when natural input values change
    document.addEventListener('input', (event) => {
      const input = event.target.closest('.natural-input');
      if (input) {
        this.preserveScrollPosition();
      }
    });

    // Preserve scroll position when natural input values change (for number inputs)
    document.addEventListener('change', (event) => {
      const input = event.target.closest('.natural-input');
      if (input) {
        this.preserveScrollPosition();
      }
    });

    // Preserve scroll position when any skill input changes
    document.addEventListener('input', (event) => {
      const input = event.target.closest('.skill-input, .skill-final-input');
      if (input) {
        this.preserveScrollPosition();
      }
    });

    // Preserve scroll position when any skill input changes (for number inputs)
    document.addEventListener('change', (event) => {
      const input = event.target.closest('.skill-input, .skill-final-input');
      if (input) {
        this.preserveScrollPosition();
      }
    });

    // Restore scroll position after DOM updates
    document.addEventListener('DOMContentLoaded', () => {
      this.restoreScrollPosition();
    });

    // Monitor for Foundry VTT's render events
    if (window.game) {
      Hooks.on('renderActorSheet', () => {
        setTimeout(() => {
          this.restoreScrollPosition();
        }, 50);
      });

      Hooks.on('updateActor', () => {
        setTimeout(() => {
          this.restoreScrollPosition();
        }, 50);
      });
    }

    // Gestion spécifique pour les fermetures de sous-menus
    document.addEventListener('click', (event) => {
      const isInSubmenu = event.target.closest('.skill-natural-submenu');
      const isToggleButton = event.target.closest('.skill-natural-toggle');
      
      // Si on clique en dehors d'un sous-menu et pas sur un bouton toggle
      if (!isInSubmenu && !isToggleButton) {
        // Préserver la position de scroll immédiatement
        const currentScroll = window.scrollY || document.documentElement.scrollTop;
        
        // Restaurer la position après un court délai
        setTimeout(() => {
          window.scrollTo(0, currentScroll);
        }, 50);
      }
    });
  }

  /**
   * Simple scroll position preservation
   */
  preserveScrollPosition() {
    this.scrollPosition = window.scrollY || document.documentElement.scrollTop;
  }

  /**
   * Simple scroll position restoration
   */
  restoreScrollPosition() {
    if (this.scrollPosition > 0) {
      window.scrollTo(0, this.scrollPosition);
    }
  }

  /**
   * Clear the preserved scroll position
   */
  clearScrollPosition() {
    this.scrollPosition = 0;
    this.isPreserving = false;
  }

  /**
   * Initialize manager when DOM is ready
   */
  static init() {
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', () => {
        new ScrollPreservationManager();
      });
    } else {
      new ScrollPreservationManager();
    }
  }
}

// Auto-initialize when the module is loaded
ScrollPreservationManager.init();
