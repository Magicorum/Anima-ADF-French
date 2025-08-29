#!/usr/bin/env python3
"""
Script pour corriger toutes les caractéristiques des compétences athlétiques
de manière précise
"""

import re

def fix_all_athletics_characteristics():
    # Lire le fichier
    with open('templates/actor/features.hbs', 'r', encoding='utf-8') as f:
        content = f.read()

    # Corrections spécifiques pour chaque compétence athlétique
    corrections = [
        # Acrobaties : DEX -> AGI
        (r'<span class=\'skill-name\'>Acrobaties</span>\s*<span class=\'skill-base-char physical-char\'>DEX</span>',
         '<span class=\'skill-name\'>Acrobaties</span>\n              <span class=\'skill-base-char physical-char\'>AGI</span>'),
        
        # Athlétisme : DEX -> AGI
        (r'<span class=\'skill-name\'>Athlétisme</span>\s*<span class=\'skill-base-char physical-char\'>DEX</span>',
         '<span class=\'skill-name\'>Athlétisme</span>\n              <span class=\'skill-base-char physical-char\'>AGI</span>'),
        
        # Escalade : DEX -> AGI
        (r'<span class=\'skill-name\'>Escalade</span>\s*<span class=\'skill-base-char physical-char\'>DEX</span>',
         '<span class=\'skill-name\'>Escalade</span>\n              <span class=\'skill-base-char physical-char\'>AGI</span>'),
        
        # Saut : DEX -> FOR
        (r'<span class=\'skill-name\'>Saut</span>\s*<span class=\'skill-base-char physical-char\'>DEX</span>',
         '<span class=\'skill-name\'>Saut</span>\n              <span class=\'skill-base-char physical-char\'>FOR</span>'),
        
        # Équitation : DEX -> AGI
        (r'<span class=\'skill-name\'>Équitation</span>\s*<span class=\'skill-base-char physical-char\'>DEX</span>',
         '<span class=\'skill-name\'>Équitation</span>\n              <span class=\'skill-base-char physical-char\'>AGI</span>'),
        
        # Natation : DEX -> AGI
        (r'<span class=\'skill-name\'>Natation</span>\s*<span class=\'skill-base-char physical-char\'>DEX</span>',
         '<span class=\'skill-name\'>Natation</span>\n              <span class=\'skill-base-char physical-char\'>AGI</span>'),
    ]

    # Appliquer les corrections
    for pattern, replacement in corrections:
        content = re.sub(pattern, replacement, content)

    # Corrections pour les modificateurs
    mod_corrections = [
        # Acrobaties : dexterity.mod -> agility.mod
        (r'<span class=\'skill-char-mod\'>\+{{system\.characteristics\.dexterity\.mod}}</span>',
         '<span class=\'skill-char-mod\'>+{{system.characteristics.agility.mod}}</span>'),
        
        # Athlétisme : dexterity.mod -> agility.mod
        (r'<span class=\'skill-char-mod\'>\+{{system\.characteristics\.dexterity\.mod}}</span>',
         '<span class=\'skill-char-mod\'>+{{system.characteristics.agility.mod}}</span>'),
        
        # Escalade : dexterity.mod -> agility.mod
        (r'<span class=\'skill-char-mod\'>\+{{system\.characteristics\.dexterity\.mod}}</span>',
         '<span class=\'skill-char-mod\'>+{{system.characteristics.agility.mod}}</span>'),
        
        # Saut : dexterity.mod -> strength.mod
        (r'<span class=\'skill-char-mod\'>\+{{system\.characteristics\.dexterity\.mod}}</span>',
         '<span class=\'skill-char-mod\'>+{{system.characteristics.strength.mod}}</span>'),
        
        # Équitation : dexterity.mod -> agility.mod
        (r'<span class=\'skill-char-mod\'>\+{{system\.characteristics\.dexterity\.mod}}</span>',
         '<span class=\'skill-char-mod\'>+{{system.characteristics.agility.mod}}</span>'),
        
        # Natation : dexterity.mod -> agility.mod
        (r'<span class=\'skill-char-mod\'>\+{{system\.characteristics\.dexterity\.mod}}</span>',
         '<span class=\'skill-char-mod\'>+{{system.characteristics.agility.mod}}</span>'),
    ]

    # Appliquer les corrections de modificateurs
    for pattern, replacement in mod_corrections:
        content = re.sub(pattern, replacement, content)

    # Écrire le fichier modifié
    with open('templates/actor/features.hbs', 'w', encoding='utf-8') as f:
        f.write(content)

    # Compter les corrections
    agi_count = len(re.findall(r'class=\'skill-base-char physical-char\'>AGI</span>', content))
    for_count = len(re.findall(r'class=\'skill-base-char physical-char\'>FOR</span>', content))
    dex_count = len(re.findall(r'class=\'skill-base-char physical-char\'>DEX</span>', content))
    
    agility_mod_count = len(re.findall(r'characteristics\.agility\.mod', content))
    strength_mod_count = len(re.findall(r'characteristics\.strength\.mod', content))
    dexterity_mod_count = len(re.findall(r'characteristics\.dexterity\.mod', content))

    print(f"✅ Corrigé toutes les caractéristiques des compétences athlétiques")
    print(f"📊 Acronymes:")
    print(f"   - AGI: {agi_count}")
    print(f"   - FOR: {for_count}")
    print(f"   - DEX: {dex_count}")
    print(f"📊 Modificateurs:")
    print(f"   - Agilité: {agility_mod_count}")
    print(f"   - Force: {strength_mod_count}")
    print(f"   - Dextérité: {dexterity_mod_count}")

if __name__ == "__main__":
    fix_all_athletics_characteristics()
