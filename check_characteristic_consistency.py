#!/usr/bin/env python3
"""
Script pour vérifier la cohérence entre l'affichage des caractéristiques et les modificateurs utilisés
"""

import re

def check_characteristic_consistency():
    # Lire le fichier
    with open('templates/actor/features.hbs', 'r', encoding='utf-8') as f:
        content = f.read()

    print("🔍 Vérification de la cohérence caractéristiques/modificateurs :")
    print("=" * 70)

    # Définir les correspondances attendues
    expected_mappings = {
        'FOR': 'strength.mod',
        'AGI': 'agility.mod', 
        'DEX': 'dexterity.mod',
        'CON': 'constitution.mod',
        'POU': 'power.mod',
        'INT': 'intelligence.mod',
        'VOL': 'will.mod',
        'PER': 'perception.mod'
    }

    # Trouver toutes les compétences avec leurs caractéristiques affichées et modificateurs
    skill_pattern = r'<span class=\'skill-base-char[^\']*\'>([A-Z]+)</span>.*?<span class=\'skill-char-mod\'>\+{{([^}]+)}}</span>'
    matches = re.findall(skill_pattern, content, re.DOTALL)

    inconsistencies = []
    correct_matches = []

    for displayed_char, used_mod in matches:
        expected_mod = expected_mappings.get(displayed_char)
        
        if expected_mod and expected_mod in used_mod:
            correct_matches.append((displayed_char, used_mod))
        else:
            inconsistencies.append((displayed_char, used_mod, expected_mod))

    print(f"\n📊 Résultats de la vérification :")
    print(f"✅ Correspondances correctes : {len(correct_matches)}")
    print(f"❌ Incohérences trouvées : {len(inconsistencies)}")

    if inconsistencies:
        print(f"\n🚨 Incohérences détectées :")
        for displayed_char, used_mod, expected_mod in inconsistencies:
            print(f"   • Affichage : {displayed_char} → Modificateur utilisé : {used_mod}")
            if expected_mod:
                print(f"     → Devrait être : {expected_mod}")
            else:
                print(f"     → Caractéristique inconnue : {displayed_char}")

    if correct_matches:
        print(f"\n✅ Correspondances correctes :")
        for displayed_char, used_mod in correct_matches[:10]:  # Afficher les 10 premières
            print(f"   • {displayed_char} → {used_mod}")

    return inconsistencies

if __name__ == "__main__":
    check_characteristic_consistency()
