#!/usr/bin/env python3
"""
Script pour ajouter automatiquement les boutons d'engrenage manquants
aux compétences secondaires dans features.hbs
"""

import re
from pathlib import Path

def get_skill_mapping():
    """Extrait le mapping compétence -> catégorie depuis config.mjs"""
    config_file = Path('module/helpers/config.mjs')
    skill_mapping = {}

    if config_file.exists():
        with open(config_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Trouver toutes les compétences avec leur baseChar
        pattern = r'(\w+):\s*{\s*name:\s*"[^"]*",\s*baseChar:\s*"(\w+)"\s*}'
        matches = re.findall(pattern, content)

        # Organiser par catégorie
        categories = {}
        for skill, baseChar in matches:
            # Déterminer la catégorie en fonction du contexte
            if f'athletics: {{{skill}:' in content:
                categories[skill] = 'athletics'
            elif f'social: {{{skill}:' in content:
                categories[skill] = 'social'
            elif f'perceptive: {{{skill}:' in content:
                categories[skill] = 'perceptive'
            elif f'intellectual: {{{skill}:' in content:
                categories[skill] = 'intellectual'
            elif f'vigor: {{{skill}:' in content:
                categories[skill] = 'vigor'
            elif f'subterfuge: {{{skill}:' in content:
                categories[skill] = 'subterfuge'
            elif f'creative: {{{skill}:' in content:
                categories[skill] = 'creative'

            skill_mapping[skill] = categories.get(skill, 'unknown')

    return skill_mapping

def add_gear_buttons():
    """Ajoute les boutons d'engrenage manquants"""

    # Lire le fichier
    with open('templates/actor/features.hbs', 'r', encoding='utf-8') as f:
        content = f.read()

    # Obtenir le mapping des compétences
    skill_mapping = get_skill_mapping()
    print(f"Mapping des compétences trouvé : {len(skill_mapping)} compétences")

    # Trouver toutes les compétences qui ont un skill-char-mod mais pas de bouton d'engrenage
    pattern = r'(<span class=\'skill-char-mod\'>[^<]*</span>\s*</div>\s*</div>)'
    matches = re.finditer(pattern, content)

    replacements_made = 0

    for match in matches:
        section_end = match.group(1)

        # Trouver le nom de la compétence dans cette section
        section_start = content.rfind('<div class=\'skill-horizontal-item\'>', 0, match.start())
        if section_start == -1:
            continue

        section = content[section_start:match.end()]

        # Extraire le nom interne de la compétence depuis data-roll
        roll_match = re.search(r'data-roll=\'1d100\+@(\w+)_base', section)
        if not roll_match:
            continue

        skill_name = roll_match.group(1)
        category = skill_mapping.get(skill_name, 'unknown')

        if category == 'unknown':
            print(f"⚠️ Catégorie inconnue pour {skill_name}")
            continue

        # Vérifier si cette compétence a déjà un bouton d'engrenage
        if f'data-skill=\'{skill_name}\'' in section:
            continue

        # Créer le bouton d'engrenage
        gear_button = f'                <button class=\'skill-natural-toggle\' data-skill=\'{skill_name}\' data-category=\'{category}\' title=\'Paramètres naturels\'>⚙️</button>'

        # Ajouter le bouton avant la fermeture de skill-values-section
        new_section_end = section_end.replace(
            '</div>\n            </div>',
            f'                {gear_button}\n            </div>\n            </div>'
        )

        # Créer la section naturelle
        natural_section = f'''          <div class='skill-natural-submenu' id='natural-submenu-{category}-{skill_name}' style='display: none;'>
            <div class='natural-inputs-row'>
              <input type='number' name='system.secondaryAbilities.{category}.{skill_name}.natural' value='{{{{system.secondaryAbilities.{category}.{skill_name}.natural}}}}' placeholder='Bonus naturel' class='natural-input' />
              <input type='number' name='system.secondaryAbilities.{category}.{skill_name}.naturalbi' value='{{{{system.secondaryAbilities.{category}.{skill_name}.naturalbi}}}}' placeholder='Bonus naturel bio' class='natural-input' />
            </div>
          </div>'''

        # Remplacer dans le contenu
        content = content.replace(section_end, new_section_end)

        # Ajouter la section naturelle après la compétence
        next_competence = content.find('<div class=\'skill-horizontal-item\'>', match.end())
        if next_competence == -1:
            next_competence = len(content)

        content = content[:next_competence] + natural_section + content[next_competence:]

        replacements_made += 1
        print(f"✅ Ajouté bouton d'engrenage pour {skill_name} ({category})")

    # Écrire le fichier modifié
    with open('templates/actor/features.hbs', 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"\n🎉 Terminé ! {replacements_made} boutons d'engrenage ajoutés.")

if __name__ == "__main__":
    add_gear_buttons()
