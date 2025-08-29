#!/usr/bin/env python3
"""
Script pour corriger spécifiquement le modificateur du Saut
"""

import re

def fix_jump_modifier():
    # Lire le fichier
    with open('templates/actor/features.hbs', 'r', encoding='utf-8') as f:
        content = f.read()

    # Corriger le modificateur du Saut : agility.mod -> strength.mod
    pattern = r'<span class=\'skill-name\'>Saut</span>.*?<span class=\'skill-char-mod\'>\+{{system\.characteristics\.agility\.mod}}</span>'
    replacement = '<span class=\'skill-name\'>Saut</span>\n              <span class=\'skill-base-char physical-char\'>FOR</span>\n            </div>\n            <div class=\'skill-values-section\'>\n              <div class=\'skill-inputs-section\'>\n                <input type=\'number\' name=\'system.secondaryAbilities.athletics.jump.value\' value=\'{{{{system.secondaryAbilities.athletics.jump.value}}}}\' placeholder=\'Final\' class=\'skill-final-input\' readonly />\n                <input type=\'number\' name=\'system.secondaryAbilities.athletics.jump.temp\' value=\'{{{{system.secondaryAbilities.athletics.jump.temp}}}}\' placeholder=\'Temp\' class=\'skill-input\' />\n                <input type=\'number\' name=\'system.secondaryAbilities.athletics.jump.special\' value=\'{{{{system.secondaryAbilities.athletics.jump.special}}}}\' placeholder=\'Spéc\' class=\'skill-input\' />\n                <input type=\'number\' name=\'system.secondaryAbilities.athletics.jump.class\' value=\'{{{{system.secondaryAbilities.athletics.jump.class}}}}\' placeholder=\'Classe\' class=\'skill-input\' />\n                <input type=\'number\' name=\'system.secondaryAbilities.athletics.jump.base\' value=\'{{{{system.secondaryAbilities.athletics.jump.base}}}}\' placeholder=\'Base\' class=\'skill-input\' />\n                <span class=\'skill-char-mod\'>+{{{{system.characteristics.strength.mod}}}}</span>'

    # Appliquer la correction
    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

    # Écrire le fichier modifié
    with open('templates/actor/features.hbs', 'w', encoding='utf-8') as f:
        f.write(new_content)

    # Vérifier la correction
    strength_mod_count = len(re.findall(r'characteristics\.strength\.mod', new_content))
    agility_mod_count = len(re.findall(r'characteristics\.agility\.mod', new_content))

    print(f"✅ Corrigé le modificateur du Saut")
    print(f"📊 Modificateurs de force: {strength_mod_count}")
    print(f"📊 Modificateurs d'agilité: {agility_mod_count}")
    print(f"🎯 Le Saut utilise maintenant le modificateur de force (FOR)")

if __name__ == "__main__":
    fix_jump_modifier()
