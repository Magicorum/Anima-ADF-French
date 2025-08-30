#!/usr/bin/env python3
"""
Script pour corriger toutes les incohérences entre l'affichage des caractéristiques et les modificateurs
"""

import re

def fix_characteristic_inconsistencies():
    # Lire le fichier
    with open('templates/actor/features.hbs', 'r', encoding='utf-8') as f:
        content = f.read()

    print("🔧 Correction des incohérences caractéristiques/modificateurs...")

    # Définir les corrections nécessaires
    corrections = [
        # willpower.mod -> will.mod (pour VOL)
        ('willpower.mod', 'will.mod'),
        # power.mod -> strength.mod (pour FOR)
        ('power.mod', 'strength.mod'),
        # power.mod -> dexterity.mod (pour DEX)
        ('power.mod', 'dexterity.mod'),
        # power.mod -> agility.mod (pour AGI)
        ('power.mod', 'agility.mod')
    ]

    # Appliquer les corrections de manière sélective
    for old_mod, new_mod in corrections:
        # Trouver les contextes où la correction doit être appliquée
        if old_mod == 'willpower.mod':
            # Remplacer willpower.mod par will.mod
            content = content.replace('willpower.mod', 'will.mod')
            print(f"   ✅ willpower.mod → will.mod")
            
        elif old_mod == 'power.mod':
            # Pour power.mod, on doit être plus sélectif
            # Chercher les contextes où power.mod est utilisé incorrectement
            
            # Pattern pour trouver les contextes où power.mod est utilisé avec FOR, DEX, AGI
            patterns = [
                # FOR avec power.mod -> strength.mod
                (r'(<span class=\'skill-base-char[^\']*\'>FOR</span>.*?<span class=\'skill-char-mod\'>\+{{[^}]*power\.mod[^}]*}})', 
                 lambda m: m.group(1).replace('power.mod', 'strength.mod')),
                
                # DEX avec power.mod -> dexterity.mod
                (r'(<span class=\'skill-base-char[^\']*\'>DEX</span>.*?<span class=\'skill-char-mod\'>\+{{[^}]*power\.mod[^}]*}})', 
                 lambda m: m.group(1).replace('power.mod', 'dexterity.mod')),
                
                # AGI avec power.mod -> agility.mod
                (r'(<span class=\'skill-base-char[^\']*\'>AGI</span>.*?<span class=\'skill-char-mod\'>\+{{[^}]*power\.mod[^}]*}})', 
                 lambda m: m.group(1).replace('power.mod', 'agility.mod'))
            ]
            
            for pattern, replacement_func in patterns:
                content = re.sub(pattern, replacement_func, content, flags=re.DOTALL)
            
            print(f"   ✅ power.mod → strength.mod (pour FOR)")
            print(f"   ✅ power.mod → dexterity.mod (pour DEX)")
            print(f"   ✅ power.mod → agility.mod (pour AGI)")

    # Écrire le fichier modifié
    with open('templates/actor/features.hbs', 'w', encoding='utf-8') as f:
        f.write(content)

    print("✅ Toutes les incohérences ont été corrigées !")
    print("🎉 Les caractéristiques affichées correspondent maintenant à leurs modificateurs")

if __name__ == "__main__":
    fix_characteristic_inconsistencies()
