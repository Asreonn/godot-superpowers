# Godot Superpowers - AI Agent Instructions

## Project Overview

Godot Superpowers is a professional-grade skill ecosystem for AI coding assistants (Claude Code, OpenCode, Codex) focused on automating Godot game development workflows.

**Current Version:** 3.0.0  
**Target Version:** 4.0.0  
**Total Skills:** 14 (3 orchestrators + 11 mini-skills)

## Architecture

### Directory Structure
```
/home/asreonn/godot-superpowers/
├── orchestrators/          # High-level coordination skills
│   ├── godot-refactor/
│   ├── godot-organize-project/
│   └── godot-fix-positions/
├── mini-skills/            # Single-purpose focused skills
│   ├── godot-extract-to-scenes/
│   ├── godot-split-scripts/
│   ├── godot-add-signals/
│   ├── godot-extract-resources/
│   ├── godot-clean-conflicts/
│   ├── godot-organize-files/
│   ├── godot-organize-assets/
│   ├── godot-organize-scripts/
│   ├── godot-sync-static-positions/
│   ├── godot-sync-camera-positions/
│   └── godot-sync-parallax/
├── docs/                   # Planning and documentation
│   ├── 01_VISION_AND_STRATEGY.md
│   ├── 02_GODOT4_REQUIREMENTS.md
│   └── 03_IMPLEMENTATION_ROADMAP.md
├── scripts/                # Validation and utility scripts
├── tests/                  # Test suite
└── test-projects/          # Sample Godot projects for testing
```

### Skill Format (SKILL.md v2.0)

Each skill must have a SKILL.md file with:
- YAML frontmatter with metadata
- Description and usage instructions
- Examples (before/after transformations)

**Required Frontmatter Fields:**
- `name`: Skill identifier
- `version`: Semantic version (x.y.z)
- `displayName`: Human-readable name
- `description`: What the skill does
- `author`: Creator name
- `license`: SPDX identifier (MIT, Apache-2.0, etc.)
- `category`: Primary category
- `type`: agent|tool|workflow
- `keywords`: Discovery tags (max 10)
- `platforms`: OS compatibility

## Implementation Roadmap

### Phase 0: Infrastructure (Week 1-2) ✅
- [x] CI/CD pipeline (GitHub Actions)
- [x] Validation scripts
- [x] Test framework (pytest)
- [ ] Test projects (sample Godot 4.x)
- [ ] AGENTS.md template

### Phase 1: Modernization (Week 3-6) - IN PROGRESS
- [ ] Update all 14 SKILL.md files with v2.0 frontmatter
- [ ] Add security permissions
- [ ] Input/output schemas
- [ ] Testing infrastructure

### Phase 2: Godot 4.x Skills (Week 7-18)
- [ ] godot-modernize-gdscript (P0)
- [ ] godot-migrate-tilemap (P0)
- [ ] godot-profile-performance (P1)
- [ ] godot-generate-tests (P1)
- [ ] godot-setup-navigation (P1)
- [ ] godot-setup-multiplayer (P1)

### Phase 3-6: See docs/03_IMPLEMENTATION_ROADMAP.md

## Commands

### Validation
```bash
# Check all skills
python scripts/validate_skills.py

# Check frontmatter completeness
python scripts/check_frontmatter.py

# Run tests
pytest tests/ -v
```

### Skill Development
```bash
# Create new skill from template
# (template script coming soon)

# Test single skill
pytest tests/test_skills.py::TestSkillStructure -v
```

## Development Guidelines

1. **Always run validation** before committing changes
2. **Follow SKILL.md v2.0** format specification
3. **Include examples** with before/after transformations
4. **Test with real Godot projects** when possible
5. **Update this AGENTS.md** when adding new conventions

## Current Status

**Active Phase:** Phase 0 - Infrastructure Setup  
**Next Milestone:** Phase 1 - Modernization (14 skill frontmatter updates)  
**Blockers:** None

## Resources

- Planning Docs: `docs/`
- Skills: `orchestrators/` and `mini-skills/`
- Validation: `scripts/`
- Tests: `tests/`
- CI/CD: `.github/workflows/`
