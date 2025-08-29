#!/usr/bin/env python3
"""
Script pour corriger l'ordre des boutons d'engrenage
"""

import re

def fix_button_order():
    """Corrige l'ordre des boutons d'engrenage par rapport aux spans skill-char-mod"""

    # Lire le fichier
    with open('templates/actor/features.hbs', 'r', encoding='utf-8') as f:
        content = f.read()

    # Pattern pour trouver les sections où le bouton vient avant le span
    # On cherche : button skill-natural-toggle ... suivi de span skill-char-mod
    pattern = r'(\s*)(<button class=\'skill-natural-toggle\'[^>]*>⚙️</button>)\s*\n(\s*)(<span class=\'skill-char-mod\'[^>]*>[^<]*</span>)'

    def swap_elements(match):
        indent1 = match.group(1)
        button = match.group(2)
        indent2 = match.group(3)
        span = match.group(4)

        # Inverser l'ordre : span d'abord, puis button
        return f'{indent2}{span}\n{indent1}{button}'

    # Appliquer le remplacement
    new_content = re.sub(pattern, swap_elements, content)

    # Écrire le fichier modifié
    with open('templates/actor/features.hbs', 'w', encoding='utf-8') as f:
        f.write(new_content)

    print("✅ Ordre des boutons d'engrenage corrigé")

if __name__ == "__main__":
    fix_button_order()
