#!/usr/bin/env python3
"""
Script pour corriger automatiquement les formules de jet des compétences secondaires
dans le fichier features.hbs
"""

import re

def fix_skill_rolls():
    # Liste des compétences secondaires à corriger
    skills = [
        'acrobatics', 'athleticism', 'climb', 'jump', 'ride', 'swim',
        'style', 'intimidate', 'leadership', 'persuasion', 'trading', 'etiquette',
        'notice', 'search', 'track',
        'animals', 'sciences', 'law', 'herbalLore', 'history', 'memorize', 'medicine', 'navigation',
        'composure', 'featsOfStrength', 'withstandPain',
        'disguise', 'hide', 'lockpicking', 'poisons', 'sleightOfHand', 'stealth', 'theft', 'trapLore',
        'alchemy', 'animism', 'art', 'dance', 'forging', 'jewelry', 'music',
        'ritualCalligraphy', 'rune', 'tailoring'
    ]

    # Lire le fichier
    with open('templates/actor/features.hbs', 'r', encoding='utf-8') as f:
        content = f.read()

    # Pour chaque compétence, remplacer la formule simple par la formule complète
    for skill in skills:
        # Pattern pour trouver les boutons de jet simples
        simple_pattern = f'1d100+@{skill}"'
        # Nouvelle formule complète
        full_formula = f'1d100+@{skill}_base+@{skill}_class+@{skill}_special+@{skill}_temp+@{skill}_natural+@{skill}_naturalbi+@{skill}_charmod+@{skill}_globalbonus"'

        # Remplacer dans le contenu
        content = content.replace(simple_pattern, full_formula)

    # Écrire le fichier modifié
    with open('templates/actor/features.hbs', 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"✅ Corrigé les formules de jet pour {len(skills)} compétences secondaires")

if __name__ == "__main__":
    fix_skill_rolls()
