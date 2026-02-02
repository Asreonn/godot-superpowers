#!/usr/bin/env python3
"""
Skill validation script for Godot Superpowers
Validates SKILL.md format compliance with v2.0 specification
"""

import os
import re
import sys
import yaml
from pathlib import Path

REQUIRED_FIELDS = [
    'name',
    'version',
    'displayName',
    'description',
    'author',
    'license',
    'category',
    'type',
]

RECOMMENDED_FIELDS = [
    'repository',
    'homepage',
    'keywords',
    'platforms',
    'difficulty',
    'audience',
]

OPTIONAL_FIELDS = [
    'authorEmail',
    'authorUrl',
    'subcategory',
    'filesystem',
    'network',
    'tools',
    'bashCommands',
    'behavior',
    'dependencies',
]

def parse_frontmatter(content):
    """Extract YAML frontmatter from markdown content"""
    pattern = r'^---\s*\n(.*?)\n---\s*\n'
    match = re.match(pattern, content, re.DOTALL)
    if match:
        try:
            return yaml.safe_load(match.group(1))
        except yaml.YAMLError as e:
            return None
    return None

def validate_skill_file(filepath):
    """Validate a single SKILL.md file"""
    errors = []
    warnings = []
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check for frontmatter
    frontmatter = parse_frontmatter(content)
    if frontmatter is None:
        errors.append("Missing or invalid YAML frontmatter")
        return errors, warnings
    
    # Check required fields
    for field in REQUIRED_FIELDS:
        if field not in frontmatter:
            errors.append(f"Missing required field: {field}")
    
    # Check recommended fields
    for field in RECOMMENDED_FIELDS:
        if field not in frontmatter:
            warnings.append(f"Missing recommended field: {field}")
    
    # Validate specific fields
    if 'version' in frontmatter:
        version = frontmatter['version']
        if not re.match(r'^\d+\.\d+\.\d+$', str(version)):
            errors.append(f"Invalid version format: {version} (should be semver: x.y.z)")
    
    if 'license' in frontmatter:
        license_val = frontmatter['license']
        valid_licenses = ['MIT', 'Apache-2.0', 'GPL-3.0', 'BSD-3-Clause', 'Proprietary']
        if license_val not in valid_licenses:
            warnings.append(f"Non-standard license: {license_val}")
    
    if 'type' in frontmatter:
        skill_type = frontmatter['type']
        valid_types = ['agent', 'tool', 'workflow']
        if skill_type not in valid_types:
            errors.append(f"Invalid type: {skill_type} (should be one of: {', '.join(valid_types)})")
    
    if 'difficulty' in frontmatter:
        difficulty = frontmatter['difficulty']
        valid_difficulties = ['beginner', 'intermediate', 'advanced']
        if difficulty not in valid_difficulties:
            errors.append(f"Invalid difficulty: {difficulty} (should be one of: {', '.join(valid_difficulties)})")
    
    return errors, warnings

def main():
    """Main validation function"""
    base_path = Path('/home/asreonn/godot-superpowers')
    
    skill_dirs = []
    skill_dirs.extend((base_path / 'orchestrators').glob('*/SKILL.md'))
    skill_dirs.extend((base_path / 'mini-skills').glob('*/SKILL.md'))
    
    total_errors = 0
    total_warnings = 0
    
    print("=" * 70)
    print("SKILL.md Validation Report")
    print("=" * 70)
    
    for skill_file in skill_dirs:
        skill_name = skill_file.parent.name
        print(f"\n📋 {skill_name}")
        print("-" * 70)
        
        errors, warnings = validate_skill_file(skill_file)
        
        if errors:
            for error in errors:
                print(f"  ❌ ERROR: {error}")
            total_errors += len(errors)
        
        if warnings:
            for warning in warnings:
                print(f"  ⚠️  WARNING: {warning}")
            total_warnings += len(warnings)
        
        if not errors and not warnings:
            print("  ✅ All checks passed")
    
    print("\n" + "=" * 70)
    print(f"Total: {len(skill_dirs)} skills checked")
    print(f"Errors: {total_errors}")
    print(f"Warnings: {total_warnings}")
    print("=" * 70)
    
    if total_errors > 0:
        print("\n❌ Validation FAILED")
        sys.exit(1)
    else:
        print("\n✅ Validation PASSED")
        sys.exit(0)

if __name__ == '__main__':
    main()
