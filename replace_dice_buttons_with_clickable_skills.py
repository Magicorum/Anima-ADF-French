#!/usr/bin/env python3
"""
Script pour remplacer les boutons de dés par des compétences cliquables
dans le fichier features.hbs
"""

import re

def replace_dice_buttons_with_clickable_skills():
    # Lire le fichier
    with open('templates/actor/features.hbs', 'r', encoding='utf-8') as f:
        content = f.read()

    # Pattern pour trouver les sections de compétences avec boutons de dés
    # Cherche le pattern: skill-name-section suivi de skill-roll-section avec bouton
    pattern = r'<div class=\'skill-name-section\'>\s*<span class=\'skill-name\'>([^<]+)</span>\s*<span class=\'skill-base-char\'>([^<]+)</span>\s*</div>\s*<div class=\'skill-values-section\'>\s*<div class=\'skill-roll-section\'>\s*<button class=\'skill-roll-btn rollable\' data-action=\'roll\' data-roll=\'([^\']+)\' data-label=\'([^\']+)\'[^>]*>🎲</button>\s*</div>'

    def replace_skill_section(match):
        skill_name = match.group(1)
        base_char = match.group(2)
        roll_formula = match.group(3)
        label = match.group(4)
        
        # Créer la nouvelle section avec le nom cliquable
        new_section = f'''<div class='skill-name-section clickable-skill' data-action='roll' data-roll='{roll_formula}' data-label='{label}' title='Jet de {skill_name}'>
              <span class='skill-name'>{skill_name}</span>
              <span class='skill-base-char'>{base_char}</span>
            </div>
            <div class='skill-values-section'>
              <div class='skill-inputs-section'>'''
        
        return new_section

    # Remplacer toutes les occurrences
    new_content = re.sub(pattern, replace_skill_section, content)

    # Écrire le fichier modifié
    with open('templates/actor/features.hbs', 'w', encoding='utf-8') as f:
        f.write(new_content)

    # Compter combien de remplacements ont été faits
    old_count = len(re.findall(r'<button class=\'skill-roll-btn rollable\'', content))
    new_count = len(re.findall(r'class=\'skill-name-section clickable-skill\'', new_content))

    print(f"✅ Remplacé {new_count} boutons de dés par des compétences cliquables")
    print(f"📊 {old_count} boutons trouvés, {new_count} sections cliquables créées")

if __name__ == "__main__":
    replace_dice_buttons_with_clickable_skills()
