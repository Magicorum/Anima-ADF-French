#!/usr/bin/env python3
"""
Script pour corriger les sections dupliquées et traiter les compétences compactes
"""

import re

def fix_duplicate_sections_and_compact_skills():
    # Lire le fichier
    with open('templates/actor/features.hbs', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Corriger les sections skill-inputs-section dupliquées
    content = re.sub(r'<div class=\'skill-inputs-section\'>\s*<div class=\'skill-inputs-section\'>', 
                     '<div class=\'skill-inputs-section\'>', content)

    # 2. Traiter les compétences compactes
    # Pattern pour les compétences compactes avec boutons de dés
    compact_pattern = r'<div class=\'skill-compact-header\'>\s*<span class=\'skill-compact-name\'>([^<]+)</span>\s*<div class=\'skill-compact-values\'>\s*<span class=\'skill-compact-final\'>[^<]*</span>\s*<button class=\'skill-compact-roll rollable\' data-action=\'roll\' data-roll=\'([^\']+)\' data-label=\'([^\']+)\'[^>]*>🎲</button>\s*</div>\s*</div>'

    def replace_compact_skill(match):
        skill_name = match.group(1)
        roll_formula = match.group(2)
        label = match.group(3)
        
        # Créer la nouvelle section compacte cliquable
        new_section = f'''<div class='skill-compact-header'>
            <span class='skill-compact-name clickable-compact-skill' data-action='roll' data-roll='{roll_formula}' data-label='{label}' title='Jet de {skill_name}'>{skill_name}</span>
            <div class='skill-compact-values'>
              <span class='skill-compact-final'>[Valeur]</span>
            </div>
          </div>'''
        
        return new_section

    # Remplacer les compétences compactes
    content = re.sub(compact_pattern, replace_compact_skill, content)

    # Écrire le fichier modifié
    with open('templates/actor/features.hbs', 'w', encoding='utf-8') as f:
        f.write(content)

    print("✅ Corrigé les sections dupliquées et traité les compétences compactes")

if __name__ == "__main__":
    fix_duplicate_sections_and_compact_skills()
