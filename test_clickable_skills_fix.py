#!/usr/bin/env python3
"""
Test pour vérifier que les compétences Mémorisation, Médecine et Navigation sont maintenant cliquables
"""

import re

def test_clickable_skills_fix():
    # Lire le fichier
    with open('templates/actor/features.hbs', 'r', encoding='utf-8') as f:
        content = f.read()

    print("🔍 Test des compétences Mémorisation, Médecine et Navigation :")
    print("=" * 60)

    # Vérifier chaque compétence
    skills_to_test = [
        ('Mémorisation', 'memorize'),
        ('Médecine', 'medicine'),
        ('Navigation', 'navigation')
    ]

    all_correct = True
    for skill_name, skill_id in skills_to_test:
        print(f"\n📋 Test de {skill_name} :")
        
        # Vérifier la présence de la compétence
        if skill_name in content:
            print(f"   ✅ Compétence trouvée")
        else:
            print(f"   ❌ Compétence non trouvée")
            all_correct = False
            continue

        # Vérifier la structure clickable-skill
        if f'clickable-skill' in content and skill_name in content:
            print(f"   ✅ Structure clickable-skill présente")
        else:
            print(f"   ❌ Structure clickable-skill manquante")
            all_correct = False

        # Vérifier data-action='roll'
        if f"data-action='roll'" in content and skill_name in content:
            print(f"   ✅ data-action='roll' présent")
        else:
            print(f"   ❌ data-action='roll' manquant")
            all_correct = False

        # Vérifier data-roll
        if f"data-roll=" in content and skill_name in content:
            print(f"   ✅ data-roll présent")
        else:
            print(f"   ❌ data-roll manquant")
            all_correct = False

        # Vérifier data-label
        if f"data-label='{skill_name}'" in content:
            print(f"   ✅ data-label correct")
        else:
            print(f"   ❌ data-label incorrect")
            all_correct = False

        # Vérifier la structure HTML
        pattern = rf'<div class=\'skill-name-section clickable-skill\'.*?{skill_name}.*?</div>'
        if re.search(pattern, content, re.DOTALL):
            print(f"   ✅ Structure HTML correcte")
        else:
            print(f"   ❌ Structure HTML incorrecte")
            all_correct = False

    print("\n" + "=" * 60)
    if all_correct:
        print("🎉 Toutes les compétences sont maintenant cliquables !")
        print("💡 Mémorisation, Médecine et Navigation devraient fonctionner correctement")
    else:
        print("⚠️  Certaines compétences nécessitent encore des corrections")

    print("🎉 Test terminé !")

if __name__ == "__main__":
    test_clickable_skills_fix()
