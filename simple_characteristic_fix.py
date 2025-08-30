#!/usr/bin/env python3
"""
Script simple et efficace pour corriger les incohérences
"""

import re

def simple_characteristic_fix():
    # Lire le fichier
    with open('templates/actor/features.hbs', 'r', encoding='utf-8') as f:
        content = f.read()

    print("🔧 Correction simple des incohérences...")

    # Corriger willpower.mod -> will.mod
    content = content.replace('willpower.mod', 'will.mod')

    # Corriger les incohérences une par une de manière simple
    # FOR avec power.mod -> strength.mod
    content = content.replace('system.characteristics.power.mod', 'system.characteristics.strength.mod')
    
    # DEX avec power.mod -> dexterity.mod
    content = content.replace('system.characteristics.power.mod', 'system.characteristics.dexterity.mod')
    
    # AGI avec power.mod -> agility.mod
    content = content.replace('system.characteristics.power.mod', 'system.characteristics.agility.mod')
    
    # POU avec strength.mod -> power.mod
    content = content.replace('system.characteristics.strength.mod', 'system.characteristics.power.mod')
    
    # POU avec dexterity.mod -> power.mod
    content = content.replace('system.characteristics.dexterity.mod', 'system.characteristics.power.mod')
    
    # POU avec agility.mod -> power.mod
    content = content.replace('system.characteristics.agility.mod', 'system.characteristics.power.mod')

    # Écrire le fichier modifié
    with open('templates/actor/features.hbs', 'w', encoding='utf-8') as f:
        f.write(content)

    print("✅ Corrections simples appliquées !")
    print("🎉 Les caractéristiques devraient maintenant être cohérentes")

if __name__ == "__main__":
    simple_characteristic_fix()
