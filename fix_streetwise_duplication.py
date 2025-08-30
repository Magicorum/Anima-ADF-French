#!/usr/bin/env python3
"""
Script pour supprimer la duplication de la compétence Conn. de la rue
"""

import re

def fix_streetwise_duplication():
    # Lire le fichier
    with open('templates/actor/features.hbs', 'r', encoding='utf-8') as f:
        content = f.read()

    # Supprimer la deuxième occurrence de la compétence Conn. de la rue
    # Garder seulement la première occurrence
    pattern = r'(<!-- Sociales - Conn\. de la rue -->.*?{{/if}}\s*)(<!-- Sociales - Conn\. de la rue -->.*?{{/if}}\s*)'
    
    # Remplacer par seulement la première occurrence
    content = re.sub(pattern, r'\1', content, flags=re.DOTALL)

    # Écrire le fichier modifié
    with open('templates/actor/features.hbs', 'w', encoding='utf-8') as f:
        f.write(content)

    print("✅ Supprimé la duplication de la compétence Conn. de la rue")
    print("🎯 Une seule occurrence reste dans le template")
    print("🎯 La compétence devrait maintenant être visible correctement")

if __name__ == "__main__":
    fix_streetwise_duplication()
