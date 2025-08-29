#!/usr/bin/env python3
"""
Script de test pour vérifier que les couleurs des caractéristiques ont été correctement implémentées
"""

import re

def test_characteristic_colors():
    # Lire le fichier
    with open('templates/actor/features.hbs', 'r', encoding='utf-8') as f:
        content = f.read()

    # Compter les différents types d'éléments
    physical_chars = len(re.findall(r'class=\'skill-base-char physical-char\'', content))
    mental_chars = len(re.findall(r'class=\'skill-base-char mental-char\'', content))
    total_skill_base_chars = len(re.findall(r'class=\'skill-base-char(?: physical-char| mental-char)?\'>[A-Z]+</span>', content))
    
    # Vérifier les caractéristiques spécifiques
    agi_count = len(re.findall(r'class=\'skill-base-char physical-char\'>AGI</span>', content))
    con_count = len(re.findall(r'class=\'skill-base-char physical-char\'>CON</span>', content))
    dex_count = len(re.findall(r'class=\'skill-base-char physical-char\'>DEX</span>', content))
    for_count = len(re.findall(r'class=\'skill-base-char physical-char\'>FOR</span>', content))
    
    int_count = len(re.findall(r'class=\'skill-base-char mental-char\'>INT</span>', content))
    per_count = len(re.findall(r'class=\'skill-base-char mental-char\'>PER</span>', content))
    pou_count = len(re.findall(r'class=\'skill-base-char mental-char\'>POU</span>', content))
    vol_count = len(re.findall(r'class=\'skill-base-char mental-char\'>VOL</span>', content))

    print("🎨 RÉSULTATS DU TEST DES COULEURS DE CARACTÉRISTIQUES")
    print("=" * 60)
    print(f"✅ Caractéristiques physiques (vert): {physical_chars}")
    print(f"✅ Caractéristiques mentales (bleu): {mental_chars}")
    print(f"📊 Total des acronymes traités: {physical_chars + mental_chars}")
    
    if total_skill_base_chars == physical_chars + mental_chars:
        print("\n🎉 SUCCÈS: Tous les acronymes ont été colorés !")
    else:
        print(f"\n⚠️  ATTENTION: {total_skill_base_chars - (physical_chars + mental_chars)} acronymes non colorés")
    
    print(f"\n🔍 Détail par caractéristique:")
    print(f"   Physiques (vert):")
    print(f"     - AGI: {agi_count}")
    print(f"     - CON: {con_count}")
    print(f"     - DEX: {dex_count}")
    print(f"     - FOR: {for_count}")
    print(f"   Mentales (bleu):")
    print(f"     - INT: {int_count}")
    print(f"     - PER: {per_count}")
    print(f"     - POU: {pou_count}")
    print(f"     - VOL: {vol_count}")
    
    # Vérifier que les styles CSS sont présents
    with open('css/anima.css', 'r', encoding='utf-8') as f:
        css_content = f.read()
    
    physical_css = len(re.findall(r'\.physical-char', css_content))
    mental_css = len(re.findall(r'\.mental-char', css_content))
    hover_physical = len(re.findall(r'\.clickable-skill:hover \.physical-char', css_content))
    hover_mental = len(re.findall(r'\.clickable-skill:hover \.mental-char', css_content))
    
    print(f"\n🎨 Styles CSS:")
    print(f"   - .physical-char: {physical_css} occurrences")
    print(f"   - .mental-char: {mental_css} occurrences")
    print(f"   - Effet de survol physique: {hover_physical} occurrences")
    print(f"   - Effet de survol mental: {hover_mental} occurrences")
    
    if physical_css > 0 and mental_css > 0 and hover_physical > 0 and hover_mental > 0:
        print("✅ Tous les styles CSS sont présents")
    else:
        print("⚠️  Styles CSS manquants")

if __name__ == "__main__":
    test_characteristic_colors()
