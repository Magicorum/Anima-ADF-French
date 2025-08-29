#!/usr/bin/env python3
"""
Script pour corriger automatiquement TOUTES les formules de jet des compétences secondaires
dans le fichier features.hbs
"""

import re

def fix_all_skill_rolls():
    # Lire le fichier
    with open('templates/actor/features.hbs', 'r', encoding='utf-8') as f:
        content = f.read()

    # Pattern pour trouver tous les boutons de jet simples (1d100+@nomcompetence)
    # qui ne contiennent pas encore "_base"
    pattern = r'1d100\+@([a-zA-Z]+)(?![\w_]*_base)'

    def replace_simple_roll(match):
        skill_name = match.group(1)
        # Nouvelle formule complète
        full_formula = f'1d100+@{skill_name}_base+@{skill_name}_class+@{skill_name}_special+@{skill_name}_temp+@{skill_name}_natural+@{skill_name}_naturalbi+@{skill_name}_charmod+@{skill_name}_globalbonus'
        return full_formula

    # Remplacer toutes les occurrences
    new_content = re.sub(pattern, replace_simple_roll, content)

    # Compter combien de remplacements ont été faits
    old_count = len(re.findall(r'1d100+@([a-zA-Z]+)(?!\w*_base)', content))
    new_count = len(re.findall(r'1d100+@([a-zA-Z]+)_base', new_content))

    # Écrire le fichier modifié
    with open('templates/actor/features.hbs', 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"✅ Corrigé {new_count} formules de jet de compétences secondaires")
    print(f"📊 {old_count} formules simples remplacées, {new_count} formules complètes créées")

if __name__ == "__main__":
    fix_all_skill_rolls()
