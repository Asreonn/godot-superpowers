# Godot Superpowers - Test Suite

import pytest
import yaml
from pathlib import Path

class TestSkillStructure:
    """Test suite for skill directory structure"""
    
    def test_orchestrators_have_skill_md(self):
        """All orchestrators must have SKILL.md"""
        base_path = Path('/home/asreonn/godot-superpowers')
        orchestrators = (base_path / 'orchestrators').glob('*/')
        
        for orch_dir in orchestrators:
            skill_file = orch_dir / 'SKILL.md'
            assert skill_file.exists(), f"Missing SKILL.md in {orch_dir.name}"
    
    def test_mini_skills_have_skill_md(self):
        """All mini-skills must have SKILL.md"""
        base_path = Path('/home/asreonn/godot-superpowers')
        mini_skills = (base_path / 'mini-skills').glob('*/')
        
        for skill_dir in mini_skills:
            skill_file = skill_dir / 'SKILL.md'
            assert skill_file.exists(), f"Missing SKILL.md in {skill_dir.name}"
    
    def test_skill_files_have_content(self):
        """All SKILL.md files must have non-empty content"""
        base_path = Path('/home/asreonn/godot-superpowers')
        skill_files = []
        skill_files.extend((base_path / 'orchestrators').glob('*/SKILL.md'))
        skill_files.extend((base_path / 'mini-skills').glob('*/SKILL.md'))
        
        for skill_file in skill_files:
            content = skill_file.read_text()
            assert len(content) > 100, f"{skill_file.parent.name} SKILL.md is too short"

class TestFrontmatter:
    """Test suite for frontmatter validation"""
    
    def parse_frontmatter(self, content):
        """Helper to parse YAML frontmatter"""
        import re
        pattern = r'^---\s*\n(.*?)\n---\s*\n'
        match = re.match(pattern, content, re.DOTALL)
        if match:
            try:
                return yaml.safe_load(match.group(1))
            except yaml.YAMLError:
                return None
        return None
    
    def test_all_skills_have_frontmatter(self):
        """All skills must have valid YAML frontmatter"""
        base_path = Path('/home/asreonn/godot-superpowers')
        skill_files = []
        skill_files.extend((base_path / 'orchestrators').glob('*/SKILL.md'))
        skill_files.extend((base_path / 'mini-skills').glob('*/SKILL.md'))
        
        for skill_file in skill_files:
            content = skill_file.read_text()
            frontmatter = self.parse_frontmatter(content)
            assert frontmatter is not None, f"{skill_file.parent.name} has invalid frontmatter"
    
    def test_frontmatter_has_required_fields(self):
        """All skills must have required frontmatter fields"""
        required_fields = ['name', 'description']
        
        base_path = Path('/home/asreonn/godot-superpowers')
        skill_files = []
        skill_files.extend((base_path / 'orchestrators').glob('*/SKILL.md'))
        skill_files.extend((base_path / 'mini-skills').glob('*/SKILL.md'))
        
        for skill_file in skill_files:
            content = skill_file.read_text()
            frontmatter = self.parse_frontmatter(content)
            
            if frontmatter:
                for field in required_fields:
                    assert field in frontmatter, \
                        f"{skill_file.parent.name} missing required field: {field}"
