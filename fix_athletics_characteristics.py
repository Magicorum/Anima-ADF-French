#!/usr/bin/env python3
"""
Script pour corriger les caractéristiques des compétences athlétiques
dans le template features.hbs
"""

import re

def fix_athletics_characteristics():
    # Lire le fichier
    with open('templates/actor/features.hbs', 'r', encoding='utf-8') as f:
        content = f.read()

    # Corrections à apporter
    corrections = [
        # Athlétisme : FOR -> AGI
        (r'<span class=\'skill-name\'>Athlétisme</span>\s*<span class=\'skill-base-char physical-char\'>FOR</span>',
         '<span class=\'skill-name\'>Athlétisme</span>\n              <span class=\'skill-base-char physical-char\'>AGI</span>'),
        
        # Escalade : FOR -> AGI
        (r'<span class=\'skill-name\'>Escalade</span>\s*<span class=\'skill-base-char physical-char\'>FOR</span>',
         '<span class=\'skill-name\'>Escalade</span>\n              <span class=\'skill-base-char physical-char\'>AGI</span>'),
        
        # Natation : FOR -> AGI
        (r'<span class=\'skill-name\'>Natation</span>\s*<span class=\'skill-base-char physical-char\'>FOR</span>',
         '<span class=\'skill-name\'>Natation</span>\n              <span class=\'skill-base-char physical-char\'>AGI</span>'),
    ]

    # Appliquer les corrections
    for pattern, replacement in corrections:
        content = re.sub(pattern, replacement, content)

    # Écrire le fichier modifié
    with open('templates/actor/features.hbs', 'w', encoding='utf-8') as f:
        f.write(content)

    # Compter les corrections
    agi_count = len(re.findall(r'class=\'skill-base-char physical-char\'>AGI</span>', content))
    for_count = len(re.findall(r'class=\'skill-base-char physical-char\'>FOR</span>', content))

    print(f"✅ Corrigé les caractéristiques des compétences athlétiques")
    print(f"📊 AGI (Agilité): {agi_count} occurrences")
    print(f"📊 FOR (Force): {for_count} occurrences")
    print(f"🎯 Athlétisme, Escalade et Natation utilisent maintenant AGI")

if __name__ == "__main__":
    fix_athletics_characteristics()
