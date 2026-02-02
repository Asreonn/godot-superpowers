# Godot Superpowers 🚀

Professional Godot project automation skills for AI coding assistants (Claude Code, OpenCode, Codex).

**Version 3.0.0** - Now with modular mini-skills architecture!

## Quick Install

### For Claude Code CLI

```bash
git clone https://github.com/asreonn/godot-superpowers.git
cd godot-superpowers

# Install all skills
cp -r mini-skills/* orchestrators/* ~/.claude/skills/
```

### For OpenCode

```bash
git clone https://github.com/asreonn/godot-superpowers.git
cd godot-superpowers

# Install all skills
cp -r mini-skills/* orchestrators/* ~/.config/opencode/skills/
```

### For Codex CLI

```bash
git clone https://github.com/asreonn/godot-superpowers.git
cd godot-superpowers

# Install all skills
cp -r mini-skills/* orchestrators/* ~/.codex/skills/
```

### Verify Installation

Restart your AI assistant and the skills will be available:

```bash
# For Claude Code
claude

# For OpenCode
opencode

# For Codex
codex
```

## What's New in v3.0

Godot Superpowers has been restructured into **mini-skills** and **orchestrators** for maximum flexibility:

- **11 focused mini-skills** - Each handles one specific operation
- **3 orchestrator skills** - Run multiple mini-skills in sequence
- **Use individually or combined** - Choose the right tool for your task

## What's Included

### Mini-Skills (Individual Operations)

Run specific operations without full refactoring workflows:

#### Code Quality Mini-Skills
- **godot-extract-to-scenes** - Convert code-created objects (Timer.new()) to .tscn files
- **godot-split-scripts** - Split monolithic scripts over 150 lines
- **godot-add-signals** - Replace get_node coupling with signals
- **godot-extract-resources** - Move const data to .tres resource files
- **godot-clean-conflicts** - Remove conflicting operations (position conflicts, duplicate signals)

#### Project Organization Mini-Skills
- **godot-organize-files** - Organize project folder structure
- **godot-organize-assets** - Organize assets by type (sprites, audio, fonts)
- **godot-organize-scripts** - Organize scripts by category (characters, enemies, components)

#### Position Sync Mini-Skills
- **godot-sync-static-positions** - Fix static position conflicts (editor vs _ready)
- **godot-sync-camera-positions** - Camera-aware positioning for backgrounds
- **godot-sync-parallax** - Parallax layer editor preview sync

### Orchestrator Skills (Run Multiple Operations)

For full project refactoring, these orchestrators run multiple mini-skills:

#### 1. godot-refactor (Code Quality)
Runs all 5 code quality mini-skills in sequence.

**Use when:**
- Full project refactoring needed
- Multiple anti-patterns detected
- Want comprehensive code cleanup

**Orchestrates:** godot-extract-to-scenes, godot-split-scripts, godot-add-signals, godot-extract-resources, godot-clean-conflicts

#### 2. godot-organize-project (Organization)
Runs all 3 organization mini-skills in sequence.

**Use when:**
- Project files scattered everywhere
- Need complete structural reorganization
- Preparing project for team collaboration

**Orchestrates:** godot-organize-files, godot-organize-assets, godot-organize-scripts

#### 3. godot-fix-positions (Position Sync)
Runs all 3 position sync mini-skills in sequence.

**Use when:**
- Multiple position conflict types
- Camera-following + parallax + static conflicts
- Want comprehensive position sync

**Orchestrates:** godot-sync-static-positions, godot-sync-camera-positions, godot-sync-parallax

## Installation Options

### Option A: Install Everything (Recommended)

```bash
# For Claude Code
cp -r mini-skills/* orchestrators/* ~/.claude/skills/

# For OpenCode
cp -r mini-skills/* orchestrators/* ~/.config/opencode/skills/

# For Codex
cp -r mini-skills/* orchestrators/* ~/.codex/skills/
```

### Option B: Install Only Mini-Skills (Granular Control)

```bash
# For Claude Code
cp -r mini-skills/* ~/.claude/skills/

# For OpenCode
cp -r mini-skills/* ~/.config/opencode/skills/

# For Codex
cp -r mini-skills/* ~/.codex/skills/
```

### Option C: Install Only Orchestrators (Simple Workflow)

```bash
# For Claude Code
cp -r orchestrators/* ~/.claude/skills/

# For OpenCode
cp -r orchestrators/* ~/.config/opencode/skills/

# For Codex
cp -r orchestrators/* ~/.codex/skills/
```

### Option D: Install Specific Skills

```bash
# Example: Install only extract-to-scenes mini-skill
# For Claude Code
cp -r mini-skills/godot-extract-to-scenes ~/.claude/skills/

# For OpenCode
cp -r mini-skills/godot-extract-to-scenes ~/.config/opencode/skills/

# For Codex
cp -r mini-skills/godot-extract-to-scenes ~/.codex/skills/
```

## How to Use

### Choosing Between Mini-Skills and Orchestrators

**Use mini-skills when:**
- You have a specific problem (e.g., "code creates timers with Timer.new()")
- Want to run one operation without full refactoring
- Need granular control over what changes

**Use orchestrators when:**
- Want comprehensive project cleanup
- Multiple operations needed
- Don't mind running full workflow

### Example: Individual Mini-Skill

```
> I have code that creates timers with Timer.new() instead of scenes

AI will invoke: godot-extract-to-scenes
Result: Only extracts Timer objects, doesn't touch anything else
```

### Example: Orchestrator

```
> Clean up my entire Godot project

AI will invoke: godot-refactor
Result: Runs all 5 code quality operations (extract, split, signals, resources, conflicts)
```

### Example: Position Sync

```
> My background follows the camera but shows wrong position in editor

AI will invoke: godot-sync-camera-positions
Result: Only syncs camera-following elements, doesn't touch static positions
```

### Common Use Cases

**Building New Features**
```
Problem: "My new code uses Timer.new() instead of scenes"
Mini-Skill: godot-extract-to-scenes
Time: ~30 seconds per component
```

**Legacy Code Cleanup**
```
Problem: "Inherited messy codebase with many issues"
Orchestrator: godot-refactor
Time: ~5-15 minutes depending on project size
```

**Level Design**
```
Problem: "Background position wrong in editor"
Mini-Skill: godot-sync-camera-positions
Time: ~10 seconds per background
```

**Team Onboarding**
```
Problem: "Need to organize project for new team member"
Orchestrator: godot-organize-project
Time: ~2-5 minutes depending on project size
```

## Requirements

- **AI Assistant** - One of:
  - [Claude Code CLI](https://github.com/anthropics/claude-code) - Official CLI from Anthropic
  - [OpenCode](https://opencode.ai/) - Open-source alternative
  - [Codex CLI](https://codex.so/) - OpenAI's CLI tool
- **Godot 4.x** - [Download from godotengine.org](https://godotengine.org/)
- **Git** - For version control
- **Unix tools** - grep, find, awk (pre-installed on Linux/Mac, included in Git Bash on Windows)

## Skills Directory Locations

Skills are automatically discovered from these directories:

| AI Assistant | Skills Directory |
|-------------|------------------|
| Claude Code | `~/.claude/skills/` |
| OpenCode | `~/.config/opencode/skills/` |
| Codex CLI | `~/.codex/skills/` |

## Features

### Modular Architecture
- Run individual operations or full workflows
- Each mini-skill is independent
- Orchestrators combine mini-skills intelligently
- Clear separation of concerns

### Intelligent Detection
- 9 decision trees for automatic node type detection
- Pattern matching on variables, properties, methods
- 80+ Godot node catalog
- Smart conflict classification

### Safety First
- Git baseline before changes
- Per-operation validation
- Automatic rollback on failure
- Iron Law: NO functional changes

## Migration from v2.x

If you're upgrading from v2.x:

**Old skill names (v2.x):**
- `godot-refactoring`
- `project-structure-organizer`
- `editor-position-sync`

**New names (v3.0):**
- `godot-refactor` (orchestrator)
- `godot-organize-project` (orchestrator)
- `godot-fix-positions` (orchestrator)

Plus 11 new mini-skills for granular operations.

**Also update installation paths:**
- Old: `~/.config/opencode/superpowers/skills/`
- New Claude Code: `~/.claude/skills/`
- New OpenCode: `~/.config/opencode/skills/`
- New Codex: `~/.codex/skills/`

See [MIGRATION.md](./MIGRATION.md) for detailed migration guide.

## Documentation

- [Migration Guide](./MIGRATION.md) - v2.x → v3.0 upgrade instructions
- [Changelog](./CHANGELOG.md) - Version history
- [Contributing](./CONTRIBUTING.md) - How to contribute
- [Orchestrators](./orchestrators/) - Full workflow documentation
- [Mini-Skills](./mini-skills/) - Individual operation documentation

## Statistics

- **14 total skills** (11 mini-skills + 3 orchestrators)
- **15,000+ lines** of comprehensive documentation
- **Compatible** with Claude Code, OpenCode, and Codex CLI
- **Production ready** and battle-tested

## Quick Start

1. Install your preferred AI assistant (Claude Code, OpenCode, or Codex)
2. Clone this repository
3. Copy skills to appropriate directory (see installation section)
4. Open your Godot project
5. Ask your AI assistant for help with specific problems
6. AI automatically invokes appropriate skills

## Resources & References

Based on official documentation and community resources:

**Claude Code:**
- [Official Documentation](https://code.claude.com/docs/en/skills)
- [Skills Setup Guide](https://code.claude.com/docs/en/setup)
- [GitHub Repository](https://github.com/anthropics/claude-code)

**OpenCode:**
- [Official Skills Documentation](https://opencode.ai/docs/skills)
- [Superpowers Framework](https://github.com/obra/superpowers)
- [OpenCode Skills Installation](https://github.com/obra/superpowers/blob/main/.opencode/INSTALL.md)

**Codex CLI:**
- [Skills in Codex](https://blog.fsck.com/2025/12/19/codex-skills/)
- [Porting Skills to Codex](https://blog.fsck.com/2025/10/27/skills-for-openai-codex/)

**Skills Marketplace:**
- [SkillsMP](https://skillsmp.com/) - 71,000+ agent skills compatible with Claude Code, Codex, and more

## License

MIT License - See [LICENSE](./LICENSE)

Godot is © Copyright 2014-present Juan Linietsky, Ariel Manzur and the Godot community.

## Contributing

Contributions welcome! See [CONTRIBUTING.md](./CONTRIBUTING.md)

## Created for the Godot Community

These skills are designed to help Godot developers maintain clean, modular projects with professional-grade automation. 💙

## Support & Issues

- 📋 [GitHub Issues](https://github.com/asreonn/godot-superpowers/issues) - Report bugs or suggest features
- 💬 [GitHub Discussions](https://github.com/asreonn/godot-superpowers/discussions) - Ask questions
- 📖 [Documentation](./orchestrators/) - Detailed guides and examples
