#!/usr/bin/env python3
"""
Script de test pour vérifier que les compétences cliquables ont été correctement implémentées
"""

import re

def test_clickable_skills():
    # Lire le fichier
    with open('templates/actor/features.hbs', 'r', encoding='utf-8') as f:
        content = f.read()

    # Compter les différents types d'éléments
    clickable_skills = len(re.findall(r'class=\'skill-name-section clickable-skill\'', content))
    clickable_compact_skills = len(re.findall(r'class=\'skill-compact-name clickable-compact-skill\'', content))
    remaining_dice_buttons = len(re.findall(r'<button class=\'skill-roll-btn rollable\'', content))
    remaining_compact_dice_buttons = len(re.findall(r'<button class=\'skill-compact-roll rollable\'', content))

    print("🔍 RÉSULTATS DU TEST DES COMPÉTENCES CLIQUABLES")
    print("=" * 50)
    print(f"✅ Compétences horizontales cliquables: {clickable_skills}")
    print(f"✅ Compétences compactes cliquables: {clickable_compact_skills}")
    print(f"⚠️  Boutons de dés restants (horizontaux): {remaining_dice_buttons}")
    print(f"⚠️  Boutons de dés restants (compacts): {remaining_compact_dice_buttons}")
    
    if remaining_dice_buttons == 0 and remaining_compact_dice_buttons == 0:
        print("\n🎉 SUCCÈS: Tous les boutons de dés ont été remplacés !")
    else:
        print(f"\n⚠️  ATTENTION: Il reste {remaining_dice_buttons + remaining_compact_dice_buttons} boutons de dés non remplacés")
    
    total_clickable = clickable_skills + clickable_compact_skills
    print(f"\n📊 Total des compétences cliquables: {total_clickable}")
    
    # Vérifier que les attributs data sont présents
    data_action_roll = len(re.findall(r'data-action=\'roll\'', content))
    data_roll = len(re.findall(r'data-roll=\'', content))
    data_label = len(re.findall(r'data-label=\'', content))
    
    print(f"\n🔧 Attributs techniques:")
    print(f"   - data-action='roll': {data_action_roll}")
    print(f"   - data-roll: {data_roll}")
    print(f"   - data-label: {data_label}")
    
    if data_action_roll == data_roll == data_label:
        print("✅ Tous les attributs techniques sont cohérents")
    else:
        print("⚠️  Incohérence dans les attributs techniques")

if __name__ == "__main__":
    test_clickable_skills()
