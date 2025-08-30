#!/usr/bin/env python3
"""
Test final pour vérifier que la compétence Conn. de la rue est correctement configurée
"""

import re

def test_streetwise_final():
    # Lire le fichier
    with open('templates/actor/features.hbs', 'r', encoding='utf-8') as f:
        content = f.read()

    print("🔍 Test final - Vérification de la compétence Conn. de la rue :")
    print("=" * 60)

    # 1. Vérifier la présence de la compétence
    print("1. Test de présence :")
    if 'Conn. de la rue' in content:
        print("   ✅ Compétence trouvée dans le template")
    else:
        print("   ❌ Compétence non trouvée")
        return

    # 2. Vérifier qu'il n'y a qu'une seule occurrence
    print("2. Test de duplication :")
    occurrences = len(re.findall(r'Conn\. de la rue', content))
    if occurrences == 2:  # Une pour le nom, une pour le titre
        print("   ✅ Une seule occurrence de la compétence")
    else:
        print(f"   ❌ {occurrences} occurrences trouvées (duplication possible)")

    # 3. Vérifier la configuration streetwise
    print("3. Test de configuration streetwise :")
    if 'system.secondaryAbilities.social.streetwise' in content:
        print("   ✅ Configuration streetwise correcte")
    else:
        print("   ❌ Configuration streetwise incorrecte")

    # 4. Vérifier le modificateur intelligence
    print("4. Test du modificateur :")
    if 'intelligence.mod' in content and 'Conn. de la rue' in content:
        print("   ✅ Modificateur intelligence correct")
    else:
        print("   ❌ Modificateur intelligence incorrect")

    # 5. Vérifier le bouton de jet
    print("5. Test du bouton de jet :")
    if 'data-label=\'Conn. de la rue\'' in content:
        print("   ✅ Bouton de jet configuré")
    else:
        print("   ❌ Bouton de jet non configuré")

    # 6. Vérifier le sous-menu naturel
    print("6. Test du sous-menu naturel :")
    if 'natural-submenu-social-streetwise' in content:
        print("   ✅ Sous-menu naturel configuré")
    else:
        print("   ❌ Sous-menu naturel non configuré")

    print("=" * 60)
    print("🎉 Test terminé !")
    print("💡 La compétence devrait maintenant être visible dans les choix sociaux")

if __name__ == "__main__":
    test_streetwise_final()
