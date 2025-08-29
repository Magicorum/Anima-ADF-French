#!/usr/bin/env python3
"""
Script pour ajouter la compétence "Connaissance de la Rue" dans la catégorie Sociales
"""

import re

def add_street_knowledge():
    # Lire le fichier
    with open('templates/actor/features.hbs', 'r', encoding='utf-8') as f:
        content = f.read()

    # Template pour la nouvelle compétence
    street_knowledge_template = '''
          <!-- Sociales - Connaissance de la Rue -->
          {{#if system.secondaryAbilities.social.streetKnowledge}}
          
          <div class='skill-natural-submenu' id='natural-submenu-social-etiquette' style='display: none;'>
            <div class='natural-inputs-row'>
              <input type='number' name='system.secondaryAbilities.social.etiquette.natural' value='{{system.secondaryAbilities.social.etiquette.natural}}' placeholder='Bonus naturel' class='natural-input' />
              <input type='number' name='system.secondaryAbilities.social.etiquette.naturalbi' value='{{system.secondaryAbilities.social.etiquette.naturalbi}}' placeholder='Bonus naturel bio' class='natural-input' />
            </div>
          </div><div class='skill-horizontal-item'>
            <div class='skill-name-section clickable-skill' data-action='roll' data-roll='1d100+@streetKnowledge_base+@streetKnowledge_class+@streetKnowledge_special+@streetKnowledge_temp+@streetKnowledge_natural_effective+@streetKnowledge_naturalbi+@streetKnowledge_charmod+@streetKnowledge_globalbonus' data-label='Connaissance de la Rue' title='Jet de Connaissance de la Rue'>
              <span class='skill-name'>Connaissance de la Rue</span>
              <span class='skill-base-char mental-char'>INT</span>
            </div>
            <div class='skill-values-section'>
              <div class='skill-inputs-section'>
                <input type='number' name='system.secondaryAbilities.social.streetKnowledge.value' value='{{system.secondaryAbilities.social.streetKnowledge.value}}' placeholder='Final' class='skill-final-input' readonly />
                <input type='number' name='system.secondaryAbilities.social.streetKnowledge.temp' value='{{system.secondaryAbilities.social.streetKnowledge.temp}}' placeholder='Temp' class='skill-input' />
                <input type='number' name='system.secondaryAbilities.social.streetKnowledge.special' value='{{system.secondaryAbilities.social.streetKnowledge.special}}' placeholder='Spéc' class='skill-input' />
                <input type='number' name='system.secondaryAbilities.social.streetKnowledge.class' value='{{system.secondaryAbilities.social.streetKnowledge.class}}' placeholder='Classe' class='skill-input' />
                <input type='number' name='system.secondaryAbilities.social.streetKnowledge.base' value='{{system.secondaryAbilities.social.streetKnowledge.base}}' placeholder='Base' class='skill-input' />
                <span class='skill-char-mod'>+{{system.characteristics.intelligence.mod}}</span>
                <button class='skill-natural-toggle' data-skill='streetKnowledge' data-category='social' title='Paramètres naturels'>⚙️</button>
              </div>
            </div>
          </div>
          {{/if}}

          <!-- Paramètres naturels pour Connaissance de la Rue -->
          {{#if system.secondaryAbilities.social.streetKnowledge}}
          <div class='skill-natural-submenu' id='natural-submenu-social-streetKnowledge' style='display: none;'>
            <div class='natural-inputs-row'>
              <input type='number' name='system.secondaryAbilities.social.streetKnowledge.natural' value='{{system.secondaryAbilities.social.streetKnowledge.natural}}' placeholder='Bonus naturel' class='natural-input' />
              <input type='number' name='system.secondaryAbilities.social.streetKnowledge.naturalbi' value='{{system.secondaryAbilities.social.streetKnowledge.naturalbi}}' placeholder='Bonus naturel bio' class='natural-input' />
            </div>
          </div>
          {{/if}}

'''

    # Trouver la position pour insérer la nouvelle compétence (après Étiquette)
    pattern = r'(<!-- Sociales - Étiquette -->.*?{{/if}}\s*)(\s*</div>\s*</div>\s*\s*<!-- Sensorielles -->)'
    
    # Remplacer par le nouveau contenu
    replacement = r'\1' + street_knowledge_template + r'\2'
    
    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

    # Écrire le fichier modifié
    with open('templates/actor/features.hbs', 'w', encoding='utf-8') as f:
        f.write(new_content)

    print("✅ Ajouté la compétence 'Connaissance de la Rue'")
    print("🎯 Caractéristique : INT (Intelligence)")
    print("🎨 Couleur : Bleu (caractéristique mentale)")
    print("📍 Position : Après Étiquette dans la catégorie Sociales")

if __name__ == "__main__":
    add_street_knowledge()
