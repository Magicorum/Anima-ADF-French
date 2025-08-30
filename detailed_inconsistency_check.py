#!/usr/bin/env python3
"""
Script pour identifier précisément où se trouvent les incohérences restantes
"""

import re

def detailed_inconsistency_check():
    # Lire le fichier
    with open('templates/actor/features.hbs', 'r', encoding='utf-8') as f:
        content = f.read()

    print("🔍 Vérification détaillée des incohérences restantes :")
    print("=" * 70)

    # Trouver toutes les compétences avec leurs caractéristiques affichées et modificateurs
    skill_pattern = r'<span class=\'skill-base-char[^\']*\'>([A-Z]+)</span>.*?<span class=\'skill-char-mod\'>\+{{([^}]+)}}</span>'
    matches = re.findall(skill_pattern, content, re.DOTALL)

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
        print(f"\n🚨 Incohérences détaillées :")
        for i, (displayed_char, used_mod, expected_mod) in enumerate(inconsistencies, 1):
            print(f"\n   {i}. Affichage : {displayed_char}")
            print(f"      Modificateur utilisé : {used_mod}")
            if expected_mod:
                print(f"      Devrait être : {expected_mod}")
            else:
                print(f"      Caractéristique inconnue : {displayed_char}")
            
            # Trouver le contexte autour de cette incohérence
            mod_name = used_mod.split(".")[-1]
            context_pattern = r'<span class=\'skill-base-char[^\']*\'>' + displayed_char + r'</span>.*?<span class=\'skill-char-mod\'>\+{{[^}]*' + mod_name + r'[^}]*}}</span>'
            context_matches = re.findall(context_pattern, content, re.DOTALL)
            
            if context_matches:
                # Extraire le nom de la compétence
                skill_name_pattern = r'<span class=\'skill-name\'>([^<]+)</span>'
                skill_name_match = re.search(skill_name_pattern, context_matches[0])
                if skill_name_match:
                    print(f"      Compétence : {skill_name_match.group(1)}")

    return inconsistencies

if __name__ == "__main__":
    detailed_inconsistency_check()
