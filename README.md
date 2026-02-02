# Godot Superpowers 🚀

Professional Godot project automation skills for Claude Code CLI.

**Version 3.0.0** - Now with modular mini-skills architecture!

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

**Orchestrates:**
- godot-extract-to-scenes
- godot-split-scripts
- godot-add-signals
- godot-extract-resources
- godot-clean-conflicts

[➡️ Read more](./orchestrators/godot-refactor/)

#### 2. godot-organize-project (Organization)
Runs all 3 organization mini-skills in sequence.

**Use when:**
- Project files scattered everywhere
- Need complete structural reorganization
- Preparing project for team collaboration

**Orchestrates:**
- godot-organize-files
- godot-organize-assets
- godot-organize-scripts

[➡️ Read more](./orchestrators/godot-organize-project/)

#### 3. godot-fix-positions (Position Sync)
Runs all 3 position sync mini-skills in sequence.

**Use when:**
- Multiple position conflict types
- Camera-following + parallax + static conflicts
- Want comprehensive position sync

**Orchestrates:**
- godot-sync-static-positions
- godot-sync-camera-positions
- godot-sync-parallax

[➡️ Read more](./orchestrators/godot-fix-positions/)

## Installation

### Step 1: Clone This Repository

```bash
git clone https://github.com/asreonn/godot-superpowers.git
cd godot-superpowers
```

### Step 2: Install Skills

Choose your installation method:

#### Option A: Install All Skills (Recommended)

```bash
# Install all mini-skills
cp -r mini-skills/* ~/.config/opencode/superpowers/skills/

# Install all orchestrators
cp -r orchestrators/* ~/.config/opencode/superpowers/skills/
```

#### Option B: Install Only Mini-Skills (Modular)

```bash
# Install only mini-skills for granular control
cp -r mini-skills/* ~/.config/opencode/superpowers/skills/
```

#### Option C: Install Only Orchestrators (Simple)

```bash
# Install only orchestrators for full workflows
cp -r orchestrators/* ~/.config/opencode/superpowers/skills/
```

#### Option D: Install Specific Skills

```bash
# Install specific mini-skills you need
cp -r mini-skills/godot-extract-to-scenes ~/.config/opencode/superpowers/skills/
cp -r mini-skills/godot-split-scripts ~/.config/opencode/superpowers/skills/

# Or specific orchestrators
cp -r orchestrators/godot-refactor ~/.config/opencode/superpowers/skills/
```

### Step 3: Verify Installation

Restart Claude Code CLI and the skills will be available.

```bash
claude
> list skills
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

Claude will invoke: godot-extract-to-scenes
Result: Only extracts Timer objects, doesn't touch anything else
```

### Example: Orchestrator

```
> Clean up my entire Godot project

Claude will invoke: godot-refactor
Result: Runs all 5 code quality operations (extract, split, signals, resources, conflicts)
```

### Example: Position Sync

```
> My background follows the camera but shows wrong position in editor

Claude will invoke: godot-sync-camera-positions
Result: Only syncs camera-following elements, doesn't touch static positions
```

### Common Use Cases

#### Building New Features
```
Problem: "My new code uses Timer.new() instead of scenes"
Mini-Skill: godot-extract-to-scenes
Time: ~30 seconds per component
```

#### Legacy Code Cleanup
```
Problem: "Inherited messy codebase with many issues"
Orchestrator: godot-refactor
Time: ~5-15 minutes depending on project size
```

#### Level Design
```
Problem: "Background position wrong in editor"
Mini-Skill: godot-sync-camera-positions
Time: ~10 seconds per background
```

#### Team Onboarding
```
Problem: "Need to organize project for new team member"
Orchestrator: godot-organize-project
Time: ~2-5 minutes depending on project size
```

## Requirements

- **Claude Code CLI** - Download from [anthropics/claude-code](https://github.com/anthropics/claude-code)
- **Godot 4.x** - Download from [godotengine.org](https://godotengine.org/)
- **Git** for version control
- Standard Unix tools (grep, find, awk)

## Documentation

### Orchestrators
- [godot-refactor](./orchestrators/godot-refactor/) - Code quality orchestrator
- [godot-organize-project](./orchestrators/godot-organize-project/) - Organization orchestrator
- [godot-fix-positions](./orchestrators/godot-fix-positions/) - Position sync orchestrator

### Mini-Skills
- [Code Quality Mini-Skills](./mini-skills/) - 5 refactoring mini-skills
- [Organization Mini-Skills](./mini-skills/) - 3 organization mini-skills
- [Position Sync Mini-Skills](./mini-skills/) - 3 position sync mini-skills

### General
- [Installation Guide](./INSTALLATION.md) - Detailed installation instructions
- [Migration Guide](./MIGRATION.md) - v2.x → v3.0 migration
- [Contributing Guide](./CONTRIBUTING.md) - How to contribute
- [Changelog](./CHANGELOG.md) - Version history

## Features Highlight

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

## Statistics

- **11 mini-skills** for focused operations
- **3 orchestrators** for full workflows
- **15,000+ lines** of comprehensive documentation
- **150+ Godot nodes** cataloged
- **Production ready** and battle-tested

## Quick Start

1. Clone the repository
2. Install mini-skills and/or orchestrators
3. Open your Godot project in Claude Code
4. Ask Claude to help with specific problems
5. Claude automatically invokes appropriate skills

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

See [MIGRATION.md](./MIGRATION.md) for detailed migration guide.

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
- 📖 [Full Documentation](./orchestrators/) - Detailed guides and examples
