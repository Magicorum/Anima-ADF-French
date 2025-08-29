#!/usr/bin/env python3
"""
Script pour corriger le template du Saut qui a des doubles accolades
"""

import re

def fix_jump_template():
    # Lire le fichier
    with open('templates/actor/features.hbs', 'r', encoding='utf-8') as f:
        content = f.read()

    # Corriger les doubles accolades dans le Saut
    corrections = [
        # Corriger les doubles accolades
        (r'{{{{system\.secondaryAbilities\.athletics\.jump\.value}}}}', '{{system.secondaryAbilities.athletics.jump.value}}'),
        (r'{{{{system\.secondaryAbilities\.athletics\.jump\.temp}}}}', '{{system.secondaryAbilities.athletics.jump.temp}}'),
        (r'{{{{system\.secondaryAbilities\.athletics\.jump\.special}}}}', '{{system.secondaryAbilities.athletics.jump.special}}'),
        (r'{{{{system\.secondaryAbilities\.athletics\.jump\.class}}}}', '{{system.secondaryAbilities.athletics.jump.class}}'),
        (r'{{{{system\.secondaryAbilities\.athletics\.jump\.base}}}}', '{{system.secondaryAbilities.athletics.jump.base}}'),
        (r'{{{{system\.characteristics\.strength\.mod}}}}', '{{system.characteristics.strength.mod}}'),
    ]

    # Appliquer les corrections
    for pattern, replacement in corrections:
        content = re.sub(pattern, replacement, content)

    # Écrire le fichier modifié
    with open('templates/actor/features.hbs', 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"✅ Corrigé les doubles accolades dans le template du Saut")
    print(f"🎯 Le Saut utilise maintenant correctement le modificateur de force (FOR)")

if __name__ == "__main__":
    fix_jump_template()
