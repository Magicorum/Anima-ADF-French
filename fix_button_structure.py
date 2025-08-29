#!/usr/bin/env python3
"""
Script pour corriger la structure HTML des boutons d'engrenage
"""

import re

def fix_button_structure():
    """Corrige la structure HTML des boutons d'engrenage"""

    # Lire le fichier
    with open('templates/actor/features.hbs', 'r', encoding='utf-8') as f:
        content = f.read()

    # Pattern pour trouver les boutons d'engrenage avec une structure incorrecte
    # On cherche : button engrenage suivi de </div>\n          </div>
    # Et on remplace par : button engrenage suivi de </div>\n            </div>

    # Cette regex est complexe car on doit gérer l'indentation et les sauts de ligne
    pattern = r'(<button class=\'skill-natural-toggle\'[^>]*>⚙️</button>)\s*</div>\s*</div>'

    def fix_structure(match):
        button = match.group(1)
        # Remplacer par la structure correcte avec la bonne indentation
        return f'{button}\n              </div>\n            </div>'

    # Appliquer le remplacement
    new_content = re.sub(pattern, fix_structure, content)

    # Écrire le fichier modifié
    with open('templates/actor/features.hbs', 'w', encoding='utf-8') as f:
        f.write(new_content)

    print("✅ Structure HTML des boutons d'engrenage corrigée")

if __name__ == "__main__":
    fix_button_structure()
