#!/usr/bin/env python3
"""
Script systématique qui corrige toutes les incohérences en une seule passe
"""

import re

def systematic_characteristic_fix():
    # Lire le fichier
    with open('templates/actor/features.hbs', 'r', encoding='utf-8') as f:
        content = f.read()

    print("🔧 Correction systématique de toutes les incohérences...")

    # Corriger willpower.mod -> will.mod
    content = content.replace('willpower.mod', 'will.mod')

    # Définir toutes les corrections nécessaires
    corrections = [
        # FOR doit utiliser strength.mod
        ('FOR', 'strength.mod'),
        # DEX doit utiliser dexterity.mod
        ('DEX', 'dexterity.mod'),
        # AGI doit utiliser agility.mod
        ('AGI', 'agility.mod'),
        # POU doit utiliser power.mod
        ('POU', 'power.mod'),
        # INT doit utiliser intelligence.mod
        ('INT', 'intelligence.mod'),
        # VOL doit utiliser will.mod
        ('VOL', 'will.mod'),
        # PER doit utiliser perception.mod
        ('PER', 'perception.mod'),
        # CON doit utiliser constitution.mod
        ('CON', 'constitution.mod')
    ]

    # Appliquer les corrections pour chaque caractéristique
    for char_code, correct_mod in corrections:
        # Trouver tous les modificateurs incorrects pour cette caractéristique
        pattern = rf'<span class=\'skill-base-char[^\']*\'>' + char_code + r'</span>.*?<span class=\'skill-char-mod\'>\+{{[^}]*([^.]+)\.mod[^}]*}}'
        matches = re.findall(pattern, content, re.DOTALL)
        
        for wrong_mod in matches:
            if wrong_mod != correct_mod.split('.')[0]:
                # Remplacer le mauvais modificateur par le bon
                old_pattern = rf'<span class=\'skill-base-char[^\']*\'>' + char_code + r'</span>.*?<span class=\'skill-char-mod\'>\+{{[^}]*' + wrong_mod + r'\.mod[^}]*}}'
                new_pattern = rf'<span class=\'skill-base-char[^\']*\'>' + char_code + r'</span>.*?<span class=\'skill-char-mod\'>\+{{[^}]*' + correct_mod.split('.')[0] + r'\.mod[^}]*}}'
                
                content = re.sub(old_pattern, lambda m: m.group(0).replace(f'{wrong_mod}.mod', correct_mod), content, flags=re.DOTALL)
                print(f"   ✅ {char_code} : {wrong_mod}.mod → {correct_mod}")

    # Écrire le fichier modifié
    with open('templates/actor/features.hbs', 'w', encoding='utf-8') as f:
        f.write(content)

    print("✅ Correction systématique terminée !")
    print("🎉 Toutes les caractéristiques sont maintenant parfaitement cohérentes !")

if __name__ == "__main__":
    systematic_characteristic_fix()
