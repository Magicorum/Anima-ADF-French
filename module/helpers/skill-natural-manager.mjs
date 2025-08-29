/**
 * Skill Natural Settings Manager
 * Handles the toggle functionality for natural skill parameters
 */
export class SkillNaturalManager {
  constructor() {
    this.activeMenus = new Set();
    this.initializeEventListeners();
  }

  /**
   * Initialize event listeners for natural toggle buttons
   */
  initializeEventListeners() {
    // Use event delegation for dynamically created elements
    document.addEventListener('click', (event) => {
      const toggleButton = event.target.closest('.skill-natural-toggle');
      const isInSubmenu = event.target.closest('.skill-natural-submenu');

      if (toggleButton) {
        this.handleToggleClick(toggleButton);
      }
      // Removed auto-close on outside click to prevent accidental closures
      // Users can now only close menus by clicking the gear button again
    });

    // Add visual feedback when hovering over submenu inputs
    document.addEventListener('focusin', (event) => {
      const input = event.target.closest('.natural-input');
      if (input) {
        input.classList.add('focused');
      }
    });

    document.addEventListener('focusout', (event) => {
      const input = event.target.closest('.natural-input');
      if (input) {
        input.classList.remove('focused');
      }
    });
  }

  /**
   * Handle toggle button click
   */
  handleToggleClick(button) {
    const skill = button.dataset.skill;
    const category = button.dataset.category;
    const submenuId = `natural-submenu-${category}-${skill}`;

    const submenu = document.getElementById(submenuId);
    if (!submenu) {
      console.warn(`Natural submenu not found: ${submenuId}`);
      return;
    }

    // Check if this menu is currently active
    if (this.activeMenus.has(submenuId)) {
      // Close the menu
      this.closeMenu(submenu, submenuId);
    } else {
      // Close any other open menus first
      this.closeAllMenus();

      // Open this menu
      this.openMenu(submenu, submenuId);
    }
  }

  /**
   * Open a natural parameters menu
   */
  openMenu(submenu, submenuId) {
    submenu.style.display = 'block';
    this.activeMenus.add(submenuId);

    // Update button visual state
    this.updateButtonState(submenuId, true);

    // Trigger animation
    setTimeout(() => {
      submenu.classList.add('menu-open');
    }, 10);
  }

  /**
   * Close a natural parameters menu
   */
  closeMenu(submenu, submenuId) {
    submenu.classList.remove('menu-open');
    submenu.classList.add('menu-closing');
    this.activeMenus.delete(submenuId);

    // Update button visual state
    this.updateButtonState(submenuId, false);

    setTimeout(() => {
      submenu.style.display = 'none';
      submenu.classList.remove('menu-closing');
    }, 200);
  }

  /**
   * Update button visual state
   */
  updateButtonState(submenuId, isOpen) {
    // Extract skill and category from submenuId
    const match = submenuId.match(/natural-submenu-(\w+)-(\w+)/);
    if (match) {
      const category = match[1];
      const skill = match[2];

      // Find the corresponding button
      const button = document.querySelector(`.skill-natural-toggle[data-skill="${skill}"][data-category="${category}"]`);
      if (button) {
        button.setAttribute('data-submenu-open', isOpen.toString());
      }
    }
  }

  /**
   * Close all open natural parameter menus
   */
  closeAllMenus() {
    this.activeMenus.forEach(submenuId => {
      const submenu = document.getElementById(submenuId);
      if (submenu) {
        this.closeMenu(submenu, submenuId);
      }
    });
    this.activeMenus.clear();

    // Also update all button states to closed
    document.querySelectorAll('.skill-natural-toggle[data-submenu-open="true"]').forEach(button => {
      button.setAttribute('data-submenu-open', 'false');
    });
  }

  /**
   * Initialize manager when DOM is ready
   */
  static init() {
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', () => {
        new SkillNaturalManager();
      });
    } else {
      new SkillNaturalManager();
    }
  }
}

// Auto-initialize when the module is loaded
SkillNaturalManager.init();
