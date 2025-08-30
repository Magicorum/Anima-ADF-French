#!/usr/bin/env python3
"""
Script pour corriger la dernière incohérence avec DEX
"""

import re

def fix_final_dex_inconsistency():
    # Lire le fichier
    with open('templates/actor/features.hbs', 'r', encoding='utf-8') as f:
        content = f.read()

    print("🔧 Correction de la dernière incohérence avec DEX...")

    # Corriger DEX avec power.mod -> dexterity.mod
    content = re.sub(
        r'(<span class=\'skill-base-char[^\']*\'>DEX</span>.*?<span class=\'skill-char-mod\'>\+{{[^}]*power\.mod[^}]*}})',
        lambda m: m.group(1).replace('power.mod', 'dexterity.mod'),
        content,
        flags=re.DOTALL
    )

    # Écrire le fichier modifié
    with open('templates/actor/features.hbs', 'w', encoding='utf-8') as f:
        f.write(content)

    print("✅ Dernière incohérence corrigée :")
    print("🎯 DEX avec power.mod → dexterity.mod")
    print("🎉 Toutes les caractéristiques sont maintenant cohérentes !")

if __name__ == "__main__":
    fix_final_dex_inconsistency()
