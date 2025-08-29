#!/usr/bin/env python3
"""
Script pour ajouter automatiquement tous les boutons d'engrenage manquants
aux compétences secondaires
"""

import re

# Mapping des compétences vers leurs catégories
skill_categories = {
    # Athletics
    'jump': 'athletics',
    'ride': 'athletics',
    'swim': 'athletics',

    # Social
    'style': 'social',
    'intimidate': 'social',
    'leadership': 'social',
    'persuasion': 'social',
    'trading': 'social',
    'etiquette': 'social',

    # Perceptive
    'notice': 'perceptive',
    'search': 'perceptive',
    'track': 'perceptive',

    # Intellectual
    'animals': 'intellectual',
    'sciences': 'intellectual',
    'law': 'intellectual',
    'herbalLore': 'intellectual',
    'history': 'intellectual',
    'tactics': 'intellectual',
    'magicAppraisal': 'intellectual',

    # Vigor
    'composure': 'vigor',
    'featsOfStrength': 'vigor',
    'withstandPain': 'vigor',

    # Subterfuge
    'disguise': 'subterfuge',
    'hide': 'subterfuge',
    'lockpicking': 'subterfuge',
    'poisons': 'subterfuge',
    'sleightOfHand': 'subterfuge',
    'stealth': 'subterfuge',
    'theft': 'subterfuge',
    'trapLore': 'subterfuge',

    # Creative
    'alchemy': 'creative',
    'animism': 'creative',
    'art': 'creative',
    'dance': 'creative',
    'forging': 'creative',
    'jewelry': 'creative',
    'music': 'creative',
    'ritualCalligraphy': 'creative',
    'rune': 'creative',
    'tailoring': 'creative'
}

def add_missing_gear_buttons():
    """Ajoute tous les boutons d'engrenage manquants"""

    # Lire le fichier
    with open('templates/actor/features.hbs', 'r', encoding='utf-8') as f:
        content = f.read()

    buttons_added = 0
    sections_added = 0

    for skill_name, category in skill_categories.items():
        # Vérifier si cette compétence a déjà un bouton d'engrenage
        if f'data-skill=\'{skill_name}\'' in content:
            continue

        # Trouver la compétence dans le fichier
        # Chercher le pattern de la compétence
        pattern = f'data-roll=\'1d100\+@{skill_name}_base'
        match = re.search(pattern, content)

        if not match:
            print(f"⚠️ Compétence {skill_name} non trouvée")
            continue

        # Trouver la fin de cette section de compétence
        start_pos = match.start()

        # Chercher le span skill-char-mod dans cette section
        search_area = content[start_pos:start_pos + 2000]
        char_mod_match = re.search(r'(<span class=\'skill-char-mod\'>[^<]*</span>\s*</div>\s*</div>)', search_area)

        if not char_mod_match:
            print(f"⚠️ Section skill-char-mod non trouvée pour {skill_name}")
            continue

        # Position absolue dans le fichier
        char_mod_pos = start_pos + char_mod_match.start()

        # Ajouter le bouton d'engrenage
        gear_button = f'                <button class=\'skill-natural-toggle\' data-skill=\'{skill_name}\' data-category=\'{category}\' title=\'Paramètres naturels\'>⚙️</button>'
        content = content[:char_mod_pos] + gear_button + '\n' + content[char_mod_pos:]

        # Trouver où ajouter la section naturelle (après la compétence)
        next_skill_pos = content.find('<div class=\'skill-horizontal-item\'>', char_mod_pos + 200)
        if next_skill_pos == -1:
            # Chercher d'autres marqueurs de fin de section
            next_skill_pos = content.find('{{/if}}', char_mod_pos + 200)
            if next_skill_pos == -1:
                next_skill_pos = char_mod_pos + 1000  # fallback

        # Créer la section naturelle
        natural_section = f'''
          <div class='skill-natural-submenu' id='natural-submenu-{category}-{skill_name}' style='display: none;'>
            <div class='natural-inputs-row'>
              <input type='number' name='system.secondaryAbilities.{category}.{skill_name}.natural' value='{{{{system.secondaryAbilities.{category}.{skill_name}.natural}}}}' placeholder='Bonus naturel' class='natural-input' />
              <input type='number' name='system.secondaryAbilities.{category}.{skill_name}.naturalbi' value='{{{{system.secondaryAbilities.{category}.{skill_name}.naturalbi}}}}' placeholder='Bonus naturel bio' class='natural-input' />
            </div>
          </div>'''

        # Insérer la section naturelle
        content = content[:next_skill_pos] + natural_section + content[next_skill_pos:]

        buttons_added += 1
        sections_added += 1
        print(f"✅ Ajouté bouton et section pour {skill_name} ({category})")

    # Écrire le fichier modifié
    with open('templates/actor/features.hbs', 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"\n🎉 Terminé ! {buttons_added} boutons d'engrenage et {sections_added} sections naturelles ajoutés.")

if __name__ == "__main__":
    add_missing_gear_buttons()
