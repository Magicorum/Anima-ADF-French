#!/usr/bin/env python3
"""
Script pour nettoyer complètement les duplications de Conn. de la rue
"""

import re

def clean_streetwise_completely():
    # Lire le fichier
    with open('templates/actor/features.hbs', 'r', encoding='utf-8') as f:
        content = f.read()

    # Supprimer toutes les occurrences de paramètres naturels dupliqués pour Conn. de la rue
    # Garder seulement la première occurrence complète
    pattern = r'(<!-- Sociales - Conn\. de la rue -->.*?<!-- Paramètres naturels pour Conn\. de la rue -->.*?{{/if}}\s*)(<!-- Paramètres naturels pour Conn\. de la rue -->.*?{{/if}}\s*)'
    
    # Remplacer par seulement la première occurrence complète
    content = re.sub(pattern, r'\1', content, flags=re.DOTALL)

    # Écrire le fichier modifié
    with open('templates/actor/features.hbs', 'w', encoding='utf-8') as f:
        f.write(content)

    print("✅ Nettoyé complètement les duplications de Conn. de la rue")
    print("🎯 Une seule occurrence complète reste dans le template")
    print("🎯 La compétence devrait maintenant être visible correctement")

if __name__ == "__main__":
    clean_streetwise_completely()
