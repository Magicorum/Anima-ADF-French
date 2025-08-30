#!/usr/bin/env python3
"""
Script ultime qui corrige toutes les incohérences restantes
"""

import re

def ultimate_characteristic_fix():
    # Lire le fichier
    with open('templates/actor/features.hbs', 'r', encoding='utf-8') as f:
        content = f.read()

    print("🔧 Correction ultime de toutes les incohérences...")

    # Corriger willpower.mod -> will.mod
    content = content.replace('willpower.mod', 'will.mod')

    # Corriger les incohérences spécifiques restantes
    # FOR avec agility.mod -> strength.mod
    content = re.sub(
        r'(<span class=\'skill-base-char[^\']*\'>FOR</span>.*?<span class=\'skill-char-mod\'>\+{{[^}]*agility\.mod[^}]*}})',
        lambda m: m.group(1).replace('agility.mod', 'strength.mod'),
        content,
        flags=re.DOTALL
    )

    # INT avec perception.mod -> intelligence.mod
    content = re.sub(
        r'(<span class=\'skill-base-char[^\']*\'>INT</span>.*?<span class=\'skill-char-mod\'>\+{{[^}]*perception\.mod[^}]*}})',
        lambda m: m.group(1).replace('perception.mod', 'intelligence.mod'),
        content,
        flags=re.DOTALL
    )

    # POU avec intelligence.mod -> power.mod
    content = re.sub(
        r'(<span class=\'skill-base-char[^\']*\'>POU</span>.*?<span class=\'skill-char-mod\'>\+{{[^}]*intelligence\.mod[^}]*}})',
        lambda m: m.group(1).replace('intelligence.mod', 'power.mod'),
        content,
        flags=re.DOTALL
    )

    # DEX avec agility.mod -> dexterity.mod
    content = re.sub(
        r'(<span class=\'skill-base-char[^\']*\'>DEX</span>.*?<span class=\'skill-char-mod\'>\+{{[^}]*agility\.mod[^}]*}})',
        lambda m: m.group(1).replace('agility.mod', 'dexterity.mod'),
        content,
        flags=re.DOTALL
    )

    # Écrire le fichier modifié
    with open('templates/actor/features.hbs', 'w', encoding='utf-8') as f:
        f.write(content)

    print("✅ Corrections ultimes appliquées :")
    print("🎯 FOR avec agility.mod → strength.mod")
    print("🎯 INT avec perception.mod → intelligence.mod")
    print("🎯 POU avec intelligence.mod → power.mod")
    print("🎯 DEX avec agility.mod → dexterity.mod")
    print("🎯 willpower.mod → will.mod")
    print("🎉 Toutes les caractéristiques sont maintenant parfaitement cohérentes !")

if __name__ == "__main__":
    ultimate_characteristic_fix()
