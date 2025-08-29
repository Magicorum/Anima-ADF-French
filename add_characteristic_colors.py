#!/usr/bin/env python3
"""
Script pour ajouter les couleurs aux acronymes des caractéristiques
dans les compétences secondaires
"""

import re

def add_characteristic_colors():
    # Lire le fichier
    with open('templates/actor/features.hbs', 'r', encoding='utf-8') as f:
        content = f.read()

    # Définir les caractéristiques physiques et mentales
    physical_chars = ['AGI', 'CON', 'DEX', 'FOR']
    mental_chars = ['INT', 'PER', 'POU', 'VOL']

    # Pattern pour trouver les acronymes de caractéristiques dans les compétences
    # Cherche <span class='skill-base-char'>ACRONYME</span>
    pattern = r'<span class=\'skill-base-char\'>([A-Z]+)</span>'

    def replace_characteristic(match):
        acronym = match.group(1)
        
        if acronym in physical_chars:
            return f'<span class=\'skill-base-char physical-char\'>{acronym}</span>'
        elif acronym in mental_chars:
            return f'<span class=\'skill-base-char mental-char\'>{acronym}</span>'
        else:
            # Garder la classe originale si ce n'est pas une caractéristique reconnue
            return match.group(0)

    # Remplacer toutes les occurrences
    new_content = re.sub(pattern, replace_characteristic, content)

    # Écrire le fichier modifié
    with open('templates/actor/features.hbs', 'w', encoding='utf-8') as f:
        f.write(new_content)

    # Compter les remplacements
    physical_count = len(re.findall(r'class=\'skill-base-char physical-char\'', new_content))
    mental_count = len(re.findall(r'class=\'skill-base-char mental-char\'', new_content))
    total_original = len(re.findall(r'class=\'skill-base-char\'>[A-Z]+</span>', content))

    print(f"✅ Ajouté les couleurs aux acronymes des caractéristiques")
    print(f"📊 Caractéristiques physiques (vert): {physical_count}")
    print(f"📊 Caractéristiques mentales (bleu): {mental_count}")
    print(f"📊 Total des acronymes traités: {physical_count + mental_count}")

if __name__ == "__main__":
    add_characteristic_colors()
