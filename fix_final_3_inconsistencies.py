#!/usr/bin/env python3
"""
Script simple pour corriger les 3 dernières incohérences
"""

import re

def fix_final_3_inconsistencies():
    # Lire le fichier
    with open('templates/actor/features.hbs', 'r', encoding='utf-8') as f:
        content = f.read()

    print("🔧 Correction des 3 dernières incohérences...")

    # Compter les occurrences avant correction
    dex_power_count = len(re.findall(r'<span class=\'skill-base-char[^\']*\'>DEX</span>.*?power\.mod', content, re.DOTALL))
    agi_power_count = len(re.findall(r'<span class=\'skill-base-char[^\']*\'>AGI</span>.*?power\.mod', content, re.DOTALL))
    
    print(f"   Avant correction : {dex_power_count} DEX avec power.mod, {agi_power_count} AGI avec power.mod")

    # Corriger DEX avec power.mod -> dexterity.mod
    content = re.sub(
        r'(<span class=\'skill-base-char[^\']*\'>DEX</span>.*?<span class=\'skill-char-mod\'>\+{{[^}]*power\.mod[^}]*}})',
        lambda m: m.group(1).replace('power.mod', 'dexterity.mod'),
        content,
        flags=re.DOTALL
    )

    # Corriger AGI avec power.mod -> agility.mod
    content = re.sub(
        r'(<span class=\'skill-base-char[^\']*\'>AGI</span>.*?<span class=\'skill-char-mod\'>\+{{[^}]*power\.mod[^}]*}})',
        lambda m: m.group(1).replace('power.mod', 'agility.mod'),
        content,
        flags=re.DOTALL
    )

    # Compter les occurrences après correction
    dex_power_count_after = len(re.findall(r'<span class=\'skill-base-char[^\']*\'>DEX</span>.*?power\.mod', content, re.DOTALL))
    agi_power_count_after = len(re.findall(r'<span class=\'skill-base-char[^\']*\'>AGI</span>.*?power\.mod', content, re.DOTALL))
    
    print(f"   Après correction : {dex_power_count_after} DEX avec power.mod, {agi_power_count_after} AGI avec power.mod")

    # Écrire le fichier modifié
    with open('templates/actor/features.hbs', 'w', encoding='utf-8') as f:
        f.write(content)

    print("✅ Corrections appliquées !")
    print("🎉 Toutes les incohérences devraient maintenant être corrigées")

if __name__ == "__main__":
    fix_final_3_inconsistencies()
