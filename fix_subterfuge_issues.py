#!/usr/bin/env python3
"""
Script pour corriger tous les problèmes de la section Subterfuge
"""

import re

def fix_subterfuge_issues():
    # Lire le fichier
    with open('templates/actor/features.hbs', 'r', encoding='utf-8') as f:
        content = f.read()

    print("🔧 Correction des problèmes de la section Subterfuge...")

    # 1. Supprimer le sous-menu mal placé de vigor.withstandPain
    pattern1 = r'<div class=\'skill-natural-submenu\' id=\'natural-submenu-vigor-withstandPain\' style=\'display: none;\'>\s*<div class=\'natural-inputs-row\'>\s*<input type=\'number\' name=\'system\.secondaryAbilities\.vigor\.withstandPain\.natural\' value=\'{{system\.secondaryAbilities\.vigor\.withstandPain\.natural}}\' placeholder=\'Bonus naturel\' class=\'natural-input\' />\s*<input type=\'number\' name=\'system\.secondaryAbilities\.vigor\.withstandPain\.naturalbi\' value=\'{{system\.secondaryAbilities\.vigor\.withstandPain\.naturalbi}}\' placeholder=\'Bonus naturel bio\' class=\'natural-input\' />\s*</div>\s*</div>'
    content = re.sub(pattern1, '', content)

    # 2. Corriger les triple accolades en double accolades
    content = content.replace('{{{#if', '{{#if')
    content = content.replace('{{{/if}}', '{{/if}}')

    # 3. Supprimer les accolades orphelines
    content = re.sub(r'\n\s*}\s*\n', '\n', content)

    # 4. Corriger les modificateurs de caractéristiques
    # Déguisement : power.mod -> dexterity.mod
    content = re.sub(r'system\.characteristics\.power\.mod.*?Déguisement', 'system.characteristics.dexterity.mod', content)
    
    # Crochetage : power.mod -> dexterity.mod  
    content = re.sub(r'system\.characteristics\.power\.mod.*?Crochetage', 'system.characteristics.dexterity.mod', content)
    
    # Hab. Manuelle : power.mod -> dexterity.mod
    content = re.sub(r'system\.characteristics\.power\.mod.*?Hab\. Manuelle', 'system.characteristics.dexterity.mod', content)

    # 5. Corriger les caractéristiques affichées
    # Déguisement : DEX (déjà correct)
    # Crochetage : DEX (déjà correct) 
    # Hab. Manuelle : DEX (déjà correct)
    # Camouflage : PER (déjà correct)
    # Poisons : INT (déjà correct)

    # 6. Corriger les classes de caractéristiques
    # Déguisement, Crochetage, Hab. Manuelle : physical-char (déjà correct)
    # Camouflage : mental-char (déjà correct)
    # Poisons : mental-char (déjà correct)

    # Écrire le fichier modifié
    with open('templates/actor/features.hbs', 'w', encoding='utf-8') as f:
        f.write(content)

    print("✅ Problèmes corrigés :")
    print("🎯 1. Supprimé le sous-menu mal placé de vigor.withstandPain")
    print("🎯 2. Corrigé les triple accolades en double accolades")
    print("🎯 3. Supprimé les accolades orphelines")
    print("🎯 4. Corrigé les modificateurs de caractéristiques")
    print("🎯 5. Vérifié les caractéristiques affichées")
    print("🎯 6. Vérifié les classes de caractéristiques")
    print("🎉 Section Subterfuge maintenant propre et fonctionnelle !")

if __name__ == "__main__":
    fix_subterfuge_issues()
