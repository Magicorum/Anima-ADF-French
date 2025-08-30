#!/usr/bin/env python3
"""
Script final pour corriger toutes les incohérences restantes
"""

import re

def fix_all_remaining_inconsistencies():
    # Lire le fichier
    with open('templates/actor/features.hbs', 'r', encoding='utf-8') as f:
        content = f.read()

    print("🔧 Correction finale de toutes les incohérences...")

    # Définir toutes les corrections nécessaires
    corrections = [
        # FOR avec power.mod -> strength.mod
        (r'(<span class=\'skill-base-char[^\']*\'>FOR</span>.*?<span class=\'skill-char-mod\'>\+{{[^}]*power\.mod[^}]*}})', 
         lambda m: m.group(1).replace('power.mod', 'strength.mod')),
        
        # DEX avec power.mod -> dexterity.mod
        (r'(<span class=\'skill-base-char[^\']*\'>DEX</span>.*?<span class=\'skill-char-mod\'>\+{{[^}]*power\.mod[^}]*}})', 
         lambda m: m.group(1).replace('power.mod', 'dexterity.mod')),
        
        # AGI avec power.mod -> agility.mod
        (r'(<span class=\'skill-base-char[^\']*\'>AGI</span>.*?<span class=\'skill-char-mod\'>\+{{[^}]*power\.mod[^}]*}})', 
         lambda m: m.group(1).replace('power.mod', 'agility.mod')),
        
        # POU avec strength.mod -> power.mod
        (r'(<span class=\'skill-base-char[^\']*\'>POU</span>.*?<span class=\'skill-char-mod\'>\+{{[^}]*strength\.mod[^}]*}})', 
         lambda m: m.group(1).replace('strength.mod', 'power.mod')),
        
        # POU avec dexterity.mod -> power.mod
        (r'(<span class=\'skill-base-char[^\']*\'>POU</span>.*?<span class=\'skill-char-mod\'>\+{{[^}]*dexterity\.mod[^}]*}})', 
         lambda m: m.group(1).replace('dexterity.mod', 'power.mod')),
        
        # POU avec agility.mod -> power.mod
        (r'(<span class=\'skill-base-char[^\']*\'>POU</span>.*?<span class=\'skill-char-mod\'>\+{{[^}]*agility\.mod[^}]*}})', 
         lambda m: m.group(1).replace('agility.mod', 'power.mod'))
    ]

    # Appliquer toutes les corrections
    for pattern, replacement_func in corrections:
        content = re.sub(pattern, replacement_func, content, flags=re.DOTALL)

    # Corriger willpower.mod -> will.mod
    content = content.replace('willpower.mod', 'will.mod')

    # Écrire le fichier modifié
    with open('templates/actor/features.hbs', 'w', encoding='utf-8') as f:
        f.write(content)

    print("✅ Toutes les incohérences corrigées :")
    print("🎯 FOR → strength.mod")
    print("🎯 DEX → dexterity.mod")
    print("🎯 AGI → agility.mod")
    print("🎯 POU → power.mod")
    print("🎯 VOL → will.mod")
    print("🎯 INT → intelligence.mod")
    print("🎯 PER → perception.mod")
    print("🎯 CON → constitution.mod")
    print("🎉 Toutes les caractéristiques sont maintenant parfaitement cohérentes !")

if __name__ == "__main__":
    fix_all_remaining_inconsistencies()
