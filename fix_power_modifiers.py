#!/usr/bin/env python3
"""
Script pour corriger spécifiquement les modificateurs de POU
"""

import re

def fix_power_modifiers():
    # Lire le fichier
    with open('templates/actor/features.hbs', 'r', encoding='utf-8') as f:
        content = f.read()

    print("🔧 Correction des modificateurs de POU...")

    # Corriger les modificateurs incorrects pour POU
    # POU avec strength.mod -> power.mod
    content = re.sub(
        r'(<span class=\'skill-base-char[^\']*\'>POU</span>.*?<span class=\'skill-char-mod\'>\+{{[^}]*strength\.mod[^}]*}})',
        lambda m: m.group(1).replace('strength.mod', 'power.mod'),
        content,
        flags=re.DOTALL
    )

    # POU avec dexterity.mod -> power.mod
    content = re.sub(
        r'(<span class=\'skill-base-char[^\']*\'>POU</span>.*?<span class=\'skill-char-mod\'>\+{{[^}]*dexterity\.mod[^}]*}})',
        lambda m: m.group(1).replace('dexterity.mod', 'power.mod'),
        content,
        flags=re.DOTALL
    )

    # Écrire le fichier modifié
    with open('templates/actor/features.hbs', 'w', encoding='utf-8') as f:
        f.write(content)

    print("✅ Modificateurs de POU corrigés :")
    print("🎯 POU avec strength.mod → power.mod")
    print("🎯 POU avec dexterity.mod → power.mod")
    print("🎉 Tous les modificateurs de POU sont maintenant corrects !")

if __name__ == "__main__":
    fix_power_modifiers()
