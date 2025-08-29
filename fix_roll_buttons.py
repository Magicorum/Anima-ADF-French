#!/usr/bin/env python3
import re

# Lire le fichier
with open('templates/actor/features.hbs', 'r', encoding='utf-8') as f:
    content = f.read()

# Pattern pour trouver les boutons de jet sans data-label
pattern = r"data-roll='1d100\+([^']+)' title='([^']+)'>\s*🎲\s*</button>"

def replace_match(match):
    roll_formula = match.group(1)
    skill_name = match.group(2)
    return f"data-roll='1d100+{roll_formula}' data-label='{skill_name}' title='Jet d&apos;{skill_name}'>🎲</button>"

# Remplacer tous les boutons de jet
new_content = re.sub(pattern, replace_match, content)

# Écrire le fichier
with open('templates/actor/features.hbs', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("✅ Tous les boutons de jet ont été mis à jour avec data-label")
