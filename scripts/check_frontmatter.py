#!/usr/bin/env python3
"""
Frontmatter completeness checker
Reports which skills need frontmatter updates for v2.0 compliance
"""

import os
import re
import yaml
from pathlib import Path
from collections import defaultdict

def parse_frontmatter(content):
    """Extract YAML frontmatter from markdown content"""
    pattern = r'^---\s*\n(.*?)\n---\s*\n'
    match = re.match(pattern, content, re.DOTALL)
    if match:
        try:
            return yaml.safe_load(match.group(1))
        except yaml.YAMLError:
            return None
    return None

def check_frontmatter_completeness():
    """Check frontmatter completeness across all skills"""
    base_path = Path('/home/asreonn/godot-superpowers')
    
    skill_dirs = []
    skill_dirs.extend((base_path / 'orchestrators').glob('*/SKILL.md'))
    skill_dirs.extend((base_path / 'mini-skills').glob('*/SKILL.md'))
    
    # Track which fields are missing
    missing_fields = defaultdict(list)
    
    required_fields = [
        'version', 'displayName', 'author', 'license', 
        'repository', 'category', 'type', 'keywords', 'platforms'
    ]
    
    print("=" * 70)
    print("Frontmatter Completeness Report")
    print("=" * 70)
    
    incomplete_count = 0
    
    for skill_file in sorted(skill_dirs):
        skill_name = skill_file.parent.name
        
        with open(skill_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        frontmatter = parse_frontmatter(content)
        
        if frontmatter is None:
            print(f"\n📋 {skill_name}")
            print(f"  ❌ No frontmatter found")
            incomplete_count += 1
            continue
        
        missing = []
        for field in required_fields:
            if field not in frontmatter:
                missing.append(field)
        
        if missing:
            print(f"\n📋 {skill_name}")
            print(f"  Missing fields: {', '.join(missing)}")
            incomplete_count += 1
            for field in missing:
                missing_fields[field].append(skill_name)
        else:
            print(f"\n📋 {skill_name}")
            print(f"  ✅ Complete")
    
    print("\n" + "=" * 70)
    print("Summary")
    print("=" * 70)
    print(f"Total skills: {len(skill_dirs)}")
    print(f"Incomplete: {incomplete_count}")
    print(f"Complete: {len(skill_dirs) - incomplete_count}")
    
    if missing_fields:
        print("\nFields needing updates across all skills:")
        for field, skills in sorted(missing_fields.items(), key=lambda x: -len(x[1])):
            print(f"  {field}: {len(skills)} skills")
    
    print("=" * 70)
    
    return incomplete_count == 0

if __name__ == '__main__':
    success = check_frontmatter_completeness()
    exit(0 if success else 1)
