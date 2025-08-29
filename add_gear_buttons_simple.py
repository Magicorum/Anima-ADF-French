#!/usr/bin/env python3
"""
Script simple pour ajouter les boutons d'engrenage manquants
en analysant directement le fichier HTML
"""

import re
from pathlib import Path

def add_gear_buttons_simple():
    """Ajoute les boutons d'engrenage manquants en analysant le HTML"""

    # Lire le fichier
    with open('templates/actor/features.hbs', 'r', encoding='utf-8') as f:
        content = f.read()

    # Mapping des noms internes vers les catégories (basé sur les patterns observés)
    category_patterns = {
        'athletics': ['acrobatics', 'athleticism', 'climb', 'jump', 'ride', 'swim'],
        'social': ['style', 'intimidate', 'leadership', 'persuasion', 'trading', 'etiquette'],
        'perceptive': ['notice', 'search', 'track'],
        'intellectual': ['animals', 'sciences', 'law', 'herbalLore', 'history', 'memorize', 'medicine', 'navigation', 'tactics', 'magicAppraisal'],
        'vigor': ['composure', 'featsOfStrength', 'withstandPain'],
        'subterfuge': ['disguise', 'hide', 'lockpicking', 'poisons', 'sleightOfHand', 'stealth', 'theft', 'trapLore'],
        'creative': ['alchemy', 'animism', 'art', 'dance', 'forging', 'jewelry', 'music', 'ritualCalligraphy', 'rune', 'tailoring']
    }

    # Créer un mapping inverse
    skill_to_category = {}
    for category, skills in category_patterns.items():
        for skill in skills:
            skill_to_category[skill] = category

    print(f"Mapping créé : {len(skill_to_category)} compétences")

    # Trouver toutes les sections de compétences qui n'ont pas de bouton d'engrenage
    # Pattern pour trouver une compétence sans bouton d'engrenage
    pattern = r'(<span class=\'skill-char-mod\'>[^<]*</span>\s*</div>\s*</div>\s*</div>)'

    def replace_func(match):
        section = match.group(1)

        # Extraire le nom de la compétence depuis data-roll
        roll_match = re.search(r'data-roll=\'1d100\+@(\w+)_base', content[match.start()-500:match.end()])
        if not roll_match:
            return match.group(1)

        skill_name = roll_match.group(1)
        category = skill_to_category.get(skill_name)

        if not category:
            print(f"⚠️ Catégorie non trouvée pour {skill_name}")
            return match.group(1)

        # Vérifier si cette compétence a déjà un bouton d'engrenage
        check_start = max(0, match.start() - 1000)
        check_section = content[check_start:match.start()]
        if f'data-skill=\'{skill_name}\'' in check_section:
            return match.group(1)

        # Créer le bouton d'engrenage
        gear_button = f'                <button class=\'skill-natural-toggle\' data-skill=\'{skill_name}\' data-category=\'{category}\' title=\'Paramètres naturels\'>⚙️</button>'

        # Ajouter le bouton
        new_section = section.replace(
            '</div>\n            </div>\n            </div>',
            f'{gear_button}\n            </div>\n            </div>\n            </div>'
        )

        print(f"✅ Bouton ajouté pour {skill_name} ({category})")
        return new_section

    # Appliquer les remplacements
    new_content = re.sub(pattern, replace_func, content)

    # Maintenant ajouter les sections naturelles
    for skill_name, category in skill_to_category.items():
        # Chercher si cette compétence a maintenant un bouton d'engrenage
        if f'data-skill=\'{skill_name}\'' in new_content:
            # Chercher la fin de cette compétence
            pattern = f'data-skill=\'{skill_name}\''
            match = re.search(pattern, new_content)
            if match:
                # Trouver la fin de cette section de compétence
                start_pos = match.start()
                # Chercher la prochaine compétence ou la fin de la section
                next_skill = new_content.find('<div class=\'skill-horizontal-item\'>', start_pos + 100)
                if next_skill == -1:
                    next_skill = len(new_content)

                # Créer la section naturelle
                natural_section = f'''          <div class='skill-natural-submenu' id='natural-submenu-{category}-{skill_name}' style='display: none;'>
            <div class='natural-inputs-row'>
              <input type='number' name='system.secondaryAbilities.{category}.{skill_name}.natural' value='{{{{system.secondaryAbilities.{category}.{skill_name}.natural}}}}' placeholder='Bonus naturel' class='natural-input' />
              <input type='number' name='system.secondaryAbilities.{category}.{skill_name}.naturalbi' value='{{{{system.secondaryAbilities.{category}.{skill_name}.naturalbi}}}}' placeholder='Bonus naturel bio' class='natural-input' />
            </div>
          </div>'''

                # Insérer la section naturelle
                new_content = new_content[:next_skill] + natural_section + new_content[next_skill:]

                print(f"✅ Section naturelle ajoutée pour {skill_name} ({category})")

    # Écrire le fichier modifié
    with open('templates/actor/features.hbs', 'w', encoding='utf-8') as f:
        f.write(new_content)

    print("\n🎉 Terminé ! Tous les boutons d'engrenage et sections naturelles ont été ajoutés.")

if __name__ == "__main__":
    add_gear_buttons_simple()
