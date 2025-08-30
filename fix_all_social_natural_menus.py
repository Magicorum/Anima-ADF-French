#!/usr/bin/env python3
"""
Script pour corriger tous les menus naturels des compétences sociales
"""

import re

def fix_all_social_natural_menus():
    # Lire le fichier
    with open('templates/actor/features.hbs', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Supprimer les sous-menus mal configurés
    # Supprimer le sous-menu mal configuré dans Commerce
    pattern1 = r'<div class=\'skill-natural-submenu\' id=\'natural-submenu-social-persuasion\' style=\'display: none;\'>\s*<div class=\'natural-inputs-row\'>\s*<input type=\'number\' name=\'system\.secondaryAbilities\.social\.persuasion\.natural\' value=\'{{system\.secondaryAbilities\.social\.persuasion\.natural}}\' placeholder=\'Bonus naturel\' class=\'natural-input\' />\s*<input type=\'number\' name=\'system\.secondaryAbilities\.social\.persuasion\.naturalbi\' value=\'{{system\.secondaryAbilities\.social\.persuasion\.naturalbi}}\' placeholder=\'Bonus naturel bio\' class=\'natural-input\' />\s*</div>\s*</div>'
    content = re.sub(pattern1, '', content)

    # Supprimer le sous-menu mal configuré dans Étiquette
    pattern2 = r'<div class=\'skill-natural-submenu\' id=\'natural-submenu-social-trading\' style=\'display: none;\'>\s*<div class=\'natural-inputs-row\'>\s*<input type=\'number\' name=\'system\.secondaryAbilities\.social\.trading\.natural\' value=\'{{system\.secondaryAbilities\.social\.trading\.natural}}\' placeholder=\'Bonus naturel\' class=\'natural-input\' />\s*<input type=\'number\' name=\'system\.secondaryAbilities\.social\.trading\.naturalbi\' value=\'{{system\.secondaryAbilities\.social\.trading\.naturalbi}}\' placeholder=\'Bonus naturel bio\' class=\'natural-input\' />\s*</div>\s*</div>'
    content = re.sub(pattern2, '', content)

    # 2. Ajouter les sous-menus naturels manquants
    # Ajouter le sous-menu pour Style après Style
    style_pattern = r'(<!-- Sociales - Style -->.*?{{/if}}\s*)'
    style_replacement = r'''\1
          <!-- Paramètres naturels pour Style -->
          {{#if system.secondaryAbilities.social.style}}
          <div class='skill-natural-submenu' id='natural-submenu-social-style' style='display: none;'>
            <div class='natural-inputs-row'>
              <input type='number' name='system.secondaryAbilities.social.style.natural' value='{{system.secondaryAbilities.social.style.natural}}' placeholder='Bonus naturel' class='natural-input' />
              <input type='number' name='system.secondaryAbilities.social.style.naturalbi' value='{{system.secondaryAbilities.social.style.naturalbi}}' placeholder='Bonus naturel bio' class='natural-input' />
            </div>
          </div>
          {{/if}}

'''
    content = re.sub(style_pattern, style_replacement, content, flags=re.DOTALL)

    # Ajouter le sous-menu pour Intimidation après Intimidation
    intimidate_pattern = r'(<!-- Sociales - Intimidation -->.*?{{/if}}\s*)'
    intimidate_replacement = r'''\1
          <!-- Paramètres naturels pour Intimidation -->
          {{#if system.secondaryAbilities.social.intimidate}}
          <div class='skill-natural-submenu' id='natural-submenu-social-intimidate' style='display: none;'>
            <div class='natural-inputs-row'>
              <input type='number' name='system.secondaryAbilities.social.intimidate.natural' value='{{system.secondaryAbilities.social.intimidate.natural}}' placeholder='Bonus naturel' class='natural-input' />
              <input type='number' name='system.secondaryAbilities.social.intimidate.naturalbi' value='{{system.secondaryAbilities.social.intimidate.naturalbi}}' placeholder='Bonus naturel bio' class='natural-input' />
            </div>
          </div>
          {{/if}}

'''
    content = re.sub(intimidate_pattern, intimidate_replacement, content, flags=re.DOTALL)

    # Ajouter le sous-menu pour Persuasion après Persuasion
    persuasion_pattern = r'(<!-- Sociales - Persuasion -->.*?{{/if}}\s*)'
    persuasion_replacement = r'''\1
          <!-- Paramètres naturels pour Persuasion -->
          {{#if system.secondaryAbilities.social.persuasion}}
          <div class='skill-natural-submenu' id='natural-submenu-social-persuasion' style='display: none;'>
            <div class='natural-inputs-row'>
              <input type='number' name='system.secondaryAbilities.social.persuasion.natural' value='{{system.secondaryAbilities.social.persuasion.natural}}' placeholder='Bonus naturel' class='natural-input' />
              <input type='number' name='system.secondaryAbilities.social.persuasion.naturalbi' value='{{system.secondaryAbilities.social.persuasion.naturalbi}}' placeholder='Bonus naturel bio' class='natural-input' />
            </div>
          </div>
          {{/if}}

'''
    content = re.sub(persuasion_pattern, persuasion_replacement, content, flags=re.DOTALL)

    # Ajouter le sous-menu pour Commerce après Commerce
    trading_pattern = r'(<!-- Sociales - Commerce -->.*?{{/if}}\s*)'
    trading_replacement = r'''\1
          <!-- Paramètres naturels pour Commerce -->
          {{#if system.secondaryAbilities.social.trading}}
          <div class='skill-natural-submenu' id='natural-submenu-social-trading' style='display: none;'>
            <div class='natural-inputs-row'>
              <input type='number' name='system.secondaryAbilities.social.trading.natural' value='{{system.secondaryAbilities.social.trading.natural}}' placeholder='Bonus naturel' class='natural-input' />
              <input type='number' name='system.secondaryAbilities.social.trading.naturalbi' value='{{system.secondaryAbilities.social.trading.naturalbi}}' placeholder='Bonus naturel bio' class='natural-input' />
            </div>
          </div>
          {{/if}}

'''
    content = re.sub(trading_pattern, trading_replacement, content, flags=re.DOTALL)

    # Ajouter le sous-menu pour Étiquette après Étiquette
    etiquette_pattern = r'(<!-- Sociales - Étiquette -->.*?{{/if}}\s*)'
    etiquette_replacement = r'''\1
          <!-- Paramètres naturels pour Étiquette -->
          {{#if system.secondaryAbilities.social.etiquette}}
          <div class='skill-natural-submenu' id='natural-submenu-social-etiquette' style='display: none;'>
            <div class='natural-inputs-row'>
              <input type='number' name='system.secondaryAbilities.social.etiquette.natural' value='{{system.secondaryAbilities.social.etiquette.natural}}' placeholder='Bonus naturel' class='natural-input' />
              <input type='number' name='system.secondaryAbilities.social.etiquette.naturalbi' value='{{system.secondaryAbilities.social.etiquette.naturalbi}}' placeholder='Bonus naturel bio' class='natural-input' />
            </div>
          </div>
          {{/if}}

'''
    content = re.sub(etiquette_pattern, etiquette_replacement, content, flags=re.DOTALL)

    # Écrire le fichier modifié
    with open('templates/actor/features.hbs', 'w', encoding='utf-8') as f:
        f.write(content)

    print("✅ Corrigé tous les menus naturels des compétences sociales :")
    print("🎯 1. Supprimé les sous-menus mal configurés")
    print("🎯 2. Ajouté les sous-menus manquants pour Style, Intimidation, Persuasion, Commerce, Étiquette")
    print("🎯 3. La Connaissance de la Rue était déjà correctement configurée")
    print("🎉 Tous les menus naturels devraient maintenant fonctionner correctement !")

if __name__ == "__main__":
    fix_all_social_natural_menus()
