#!/usr/bin/env python3
"""
Script ciblé qui corrige les incohérences de manière spécifique
"""

import re

def targeted_characteristic_fix():
    # Lire le fichier
    with open('templates/actor/features.hbs', 'r', encoding='utf-8') as f:
        content = f.read()

    print("🔧 Correction ciblée des incohérences...")

    # Corriger willpower.mod -> will.mod
    content = content.replace('willpower.mod', 'will.mod')

    # Corriger les incohérences de manière ciblée
    # FOR avec power.mod -> strength.mod
    content = re.sub(
        r'(<span class=\'skill-base-char[^\']*\'>FOR</span>.*?<span class=\'skill-char-mod\'>\+{{[^}]*power\.mod[^}]*}})',
        lambda m: m.group(1).replace('power.mod', 'strength.mod'),
        content,
        flags=re.DOTALL
    )

    # DEX avec power.mod -> dexterity.mod
    content = re.sub(
        r'(<span class=\'skill-base-char[^\']*\'>DEX</span>.*?<span class=\'skill-char-mod\'>\+{{[^}]*power\.mod[^}]*}})',
        lambda m: m.group(1).replace('power.mod', 'dexterity.mod'),
        content,
        flags=re.DOTALL
    )

    # AGI avec power.mod -> agility.mod
    content = re.sub(
        r'(<span class=\'skill-base-char[^\']*\'>AGI</span>.*?<span class=\'skill-char-mod\'>\+{{[^}]*power\.mod[^}]*}})',
        lambda m: m.group(1).replace('power.mod', 'agility.mod'),
        content,
        flags=re.DOTALL
    )

    # Écrire le fichier modifié
    with open('templates/actor/features.hbs', 'w', encoding='utf-8') as f:
        f.write(content)

    print("✅ Corrections ciblées appliquées !")
    print("🎯 FOR avec power.mod → strength.mod")
    print("🎯 DEX avec power.mod → dexterity.mod")
    print("🎯 AGI avec power.mod → agility.mod")
    print("🎯 willpower.mod → will.mod")
    print("🎉 Les caractéristiques devraient maintenant être cohérentes")

if __name__ == "__main__":
    targeted_characteristic_fix()
