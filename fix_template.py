#!/usr/bin/env python3
import json
import re

def add_natural_fields():
    # Read the template file
    with open('template.json', 'r', encoding='utf-8') as f:
        template = json.load(f)

    # Function to add natural fields to a skill if they don't exist
    def add_natural_to_skill(skill):
        if 'natural' not in skill:
            skill['natural'] = 0
        if 'naturalbi' not in skill:
            skill['naturalbi'] = 0
        return skill

    # Process all secondary abilities
    if 'secondaryAbilities' in template:
        for category, skills in template['secondaryAbilities'].items():
            if isinstance(skills, dict):
                for skill_key, skill in skills.items():
                    if isinstance(skill, dict):
                        template['secondaryAbilities'][category][skill_key] = add_natural_to_skill(skill)

    # Write back to file
    with open('template.json', 'w', encoding='utf-8') as f:
        json.dump(template, f, indent=2, ensure_ascii=False)

    print("Natural fields added to all skills")

if __name__ == "__main__":
    add_natural_fields()
