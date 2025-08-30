#!/usr/bin/env python3
"""
Script final qui corrige toutes les incohérences de manière précise
"""

import re

def final_characteristic_fix():
    # Lire le fichier
    with open('templates/actor/features.hbs', 'r', encoding='utf-8') as f:
        content = f.read()

    print("🔧 Correction finale et précise de toutes les incohérences...")

    # Définir toutes les corrections nécessaires de manière précise
    corrections = [
        # FOR doit utiliser strength.mod
        (r'(<span class=\'skill-base-char[^\']*\'>FOR</span>.*?<span class=\'skill-char-mod\'>\+{{[^}]*)(power|dexterity|agility|intelligence|will|perception|constitution)\.mod([^}]*}})', 
         r'\1strength.mod\3'),
        
        # DEX doit utiliser dexterity.mod
        (r'(<span class=\'skill-base-char[^\']*\'>DEX</span>.*?<span class=\'skill-char-mod\'>\+{{[^}]*)(power|strength|agility|intelligence|will|perception|constitution)\.mod([^}]*}})', 
         r'\1dexterity.mod\3'),
        
        # AGI doit utiliser agility.mod
        (r'(<span class=\'skill-base-char[^\']*\'>AGI</span>.*?<span class=\'skill-char-mod\'>\+{{[^}]*)(power|strength|dexterity|intelligence|will|perception|constitution)\.mod([^}]*}})', 
         r'\1agility.mod\3'),
        
        # POU doit utiliser power.mod
        (r'(<span class=\'skill-base-char[^\']*\'>POU</span>.*?<span class=\'skill-char-mod\'>\+{{[^}]*)(strength|dexterity|agility|intelligence|will|perception|constitution)\.mod([^}]*}})', 
         r'\1power.mod\3'),
        
        # INT doit utiliser intelligence.mod
        (r'(<span class=\'skill-base-char[^\']*\'>INT</span>.*?<span class=\'skill-char-mod\'>\+{{[^}]*)(power|strength|dexterity|agility|will|perception|constitution)\.mod([^}]*}})', 
         r'\1intelligence.mod\3'),
        
        # VOL doit utiliser will.mod
        (r'(<span class=\'skill-base-char[^\']*\'>VOL</span>.*?<span class=\'skill-char-mod\'>\+{{[^}]*)(power|strength|dexterity|agility|intelligence|perception|constitution)\.mod([^}]*}})', 
         r'\1will.mod\3'),
        
        # PER doit utiliser perception.mod
        (r'(<span class=\'skill-base-char[^\']*\'>PER</span>.*?<span class=\'skill-char-mod\'>\+{{[^}]*)(power|strength|dexterity|agility|intelligence|will|constitution)\.mod([^}]*}})', 
         r'\1perception.mod\3'),
        
        # CON doit utiliser constitution.mod
        (r'(<span class=\'skill-base-char[^\']*\'>CON</span>.*?<span class=\'skill-char-mod\'>\+{{[^}]*)(power|strength|dexterity|agility|intelligence|will|perception)\.mod([^}]*}})', 
         r'\1constitution.mod\3')
    ]

    # Appliquer toutes les corrections
    for pattern, replacement in corrections:
        content = re.sub(pattern, replacement, content, flags=re.DOTALL)

    # Corriger willpower.mod -> will.mod
    content = content.replace('willpower.mod', 'will.mod')

    # Écrire le fichier modifié
    with open('templates/actor/features.hbs', 'w', encoding='utf-8') as f:
        f.write(content)

    print("✅ Toutes les incohérences corrigées de manière précise !")
    print("🎯 FOR → strength.mod")
    print("🎯 DEX → dexterity.mod")
    print("🎯 AGI → agility.mod")
    print("🎯 POU → power.mod")
    print("🎯 INT → intelligence.mod")
    print("🎯 VOL → will.mod")
    print("🎯 PER → perception.mod")
    print("🎯 CON → constitution.mod")
    print("🎉 Toutes les caractéristiques sont maintenant parfaitement cohérentes !")

if __name__ == "__main__":
    final_characteristic_fix()
