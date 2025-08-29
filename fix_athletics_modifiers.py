#!/usr/bin/env python3
"""
Script pour corriger les modificateurs de caractéristiques des compétences athlétiques
dans le template features.hbs
"""

import re

def fix_athletics_modifiers():
    # Lire le fichier
    with open('templates/actor/features.hbs', 'r', encoding='utf-8') as f:
        content = f.read()

    # Corrections à apporter pour les modificateurs
    corrections = [
        # Athlétisme : strength.mod -> agility.mod
        (r'<span class=\'skill-char-mod\'>\+{{system\.characteristics\.strength\.mod}}</span>',
         '<span class=\'skill-char-mod\'>+{{system.characteristics.agility.mod}}</span>'),
        
        # Escalade : strength.mod -> agility.mod
        (r'<span class=\'skill-char-mod\'>\+{{system\.characteristics\.strength\.mod}}</span>',
         '<span class=\'skill-char-mod\'>+{{system.characteristics.agility.mod}}</span>'),
        
        # Natation : strength.mod -> agility.mod
        (r'<span class=\'skill-char-mod\'>\+{{system\.characteristics\.strength\.mod}}</span>',
         '<span class=\'skill-char-mod\'>+{{system.characteristics.agility.mod}}</span>'),
    ]

    # Appliquer les corrections
    for pattern, replacement in corrections:
        content = re.sub(pattern, replacement, content)

    # Écrire le fichier modifié
    with open('templates/actor/features.hbs', 'w', encoding='utf-8') as f:
        f.write(content)

    # Compter les corrections
    agility_mod_count = len(re.findall(r'characteristics\.agility\.mod', content))
    strength_mod_count = len(re.findall(r'characteristics\.strength\.mod', content))

    print(f"✅ Corrigé les modificateurs de caractéristiques des compétences athlétiques")
    print(f"📊 Modificateurs d'agilité: {agility_mod_count}")
    print(f"📊 Modificateurs de force: {strength_mod_count}")
    print(f"🎯 Athlétisme, Escalade et Natation utilisent maintenant le modificateur d'agilité")

if __name__ == "__main__":
    fix_athletics_modifiers()
