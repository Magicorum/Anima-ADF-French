#!/usr/bin/env python3
"""
Script pour corriger la configuration de la Connaissance de la Rue
en utilisant streetwise au lieu de streetKnowledge
"""

import re

def fix_streetwise_config():
    # Lire le fichier
    with open('templates/actor/features.hbs', 'r', encoding='utf-8') as f:
        content = f.read()

    # Remplacer toutes les occurrences de streetKnowledge par streetwise
    replacements = [
        # Remplacer les noms de champs
        (r'system\.secondaryAbilities\.social\.streetKnowledge', 'system.secondaryAbilities.social.streetwise'),
        # Remplacer les variables de jet
        (r'@streetKnowledge_', '@streetwise_'),
        # Remplacer les IDs de sous-menu
        (r'natural-submenu-social-streetKnowledge', 'natural-submenu-social-streetwise'),
        # Remplacer les data-skill
        (r'data-skill=\'streetKnowledge\'', 'data-skill=\'streetwise\''),
        # Remplacer le nom affiché
        (r'Connaissance de la Rue', 'Conn. de la rue')
    ]

    # Appliquer les remplacements
    for pattern, replacement in replacements:
        content = re.sub(pattern, replacement, content)

    # Écrire le fichier modifié
    with open('templates/actor/features.hbs', 'w', encoding='utf-8') as f:
        f.write(content)

    print("✅ Corrigé la configuration de la Connaissance de la Rue")
    print("🎯 Changé streetKnowledge -> streetwise")
    print("🎯 Changé 'Connaissance de la Rue' -> 'Conn. de la rue'")
    print("🎯 La compétence devrait maintenant être visible dans les choix sociaux")

if __name__ == "__main__":
    fix_streetwise_config()
