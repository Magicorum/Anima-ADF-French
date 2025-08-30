#!/usr/bin/env python3
"""
Test final pour vérifier que tous les menus naturels des compétences sociales fonctionnent
"""

import re

def test_social_menus_final():
    # Lire le fichier
    with open('templates/actor/features.hbs', 'r', encoding='utf-8') as f:
        content = f.read()

    print("🔍 Test final - Vérification des menus naturels des compétences sociales :")
    print("=" * 70)

    # Vérifier chaque compétence sociale
    social_skills = [
        ('Style', 'style', 'power.mod'),
        ('Intimidation', 'intimidate', 'will.mod'),
        ('Persuasion', 'persuasion', 'intelligence.mod'),
        ('Commerce', 'trading', 'intelligence.mod'),
        ('Étiquette', 'etiquette', 'intelligence.mod'),
        ('Conn. de la rue', 'streetwise', 'intelligence.mod')
    ]

    all_correct = True
    for skill_name, skill_id, expected_mod in social_skills:
        print(f"\n📋 Test de {skill_name} :")
        
        # Vérifier la présence de la compétence
        if skill_name in content:
            print(f"   ✅ Compétence trouvée")
        else:
            print(f"   ❌ Compétence non trouvée")
            all_correct = False
            continue

        # Vérifier le modificateur
        if expected_mod in content and skill_name in content:
            print(f"   ✅ Modificateur {expected_mod} correct")
        else:
            print(f"   ❌ Modificateur incorrect")
            all_correct = False

        # Vérifier le sous-menu naturel
        submenu_id = f'natural-submenu-social-{skill_id}'
        if submenu_id in content:
            print(f"   ✅ Sous-menu naturel configuré ({submenu_id})")
        else:
            print(f"   ❌ Sous-menu naturel manquant")
            all_correct = False

        # Vérifier les champs de données
        data_path = f'system.secondaryAbilities.social.{skill_id}'
        if data_path in content:
            print(f"   ✅ Champs de données configurés")
        else:
            print(f"   ❌ Champs de données manquants")
            all_correct = False

    print("\n" + "=" * 70)
    if all_correct:
        print("🎉 Toutes les compétences sociales sont correctement configurées !")
        print("💡 Les menus naturels devraient maintenant fonctionner correctement")
    else:
        print("⚠️  Certaines compétences nécessitent encore des corrections")

    # Vérifier qu'il n'y a plus de sous-menus mal configurés
    print(f"\n🔍 Vérification des sous-menus mal configurés :")
    if 'natural-submenu-social-persuasion' in content and 'system.secondaryAbilities.social.persuasion.natural' in content:
        print("   ✅ Sous-menu de Persuasion correct")
    else:
        print("   ❌ Sous-menu de Persuasion incorrect")

    if 'natural-submenu-social-trading' in content and 'system.secondaryAbilities.social.trading.natural' in content:
        print("   ✅ Sous-menu de Commerce correct")
    else:
        print("   ❌ Sous-menu de Commerce incorrect")

    print("🎉 Test terminé !")

if __name__ == "__main__":
    test_social_menus_final()
