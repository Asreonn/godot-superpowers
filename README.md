# Godot Superpowers 🚀

Professional Godot project automation skills for Claude Code CLI.

## What's Included

### 1. Godot Superpowers - Refactoring
Automatically refactor Godot projects to clean, modular architecture with zero functional changes.

**Features:**
- Extract code-created nodes to modular components
- Intelligent node selection with 90%+ confidence
- Automatic component library building
- Split monolithic scripts
- Signal-based decoupling
- Data extraction to resources

[➡️ Read more](./godot-refactoring/)

### 2. Godot Superpowers - Project Structure
Scan and intelligently reorganize project folder structure for optimal organization.

**Features:**
- Automatic project structure analysis
- Smart file categorization
- Directory hierarchy creation
- Reference auto-updating
- Full rollback support

[➡️ Read more](./project-structure-organizer/)

## Installation

### Step 1: Clone This Repository

```bash
git clone https://github.com/asreonn/godot-superpowers.git
cd godot-superpowers
```

### Step 2: Install Godot Superpowers Skills

Choose your installation method below:

#### Option A: Install Both Skills

```bash
# Copy both skills to your Claude Code skills directory
cp -r godot-refactoring ~/.config/opencode/superpowers/skills/
cp project-structure-organizer/SKILL.md ~/.config/opencode/superpowers/skills/project-structure-organizer.md
```

#### Option B: Install Only Refactoring Skill

```bash
# Copy just the refactoring skill
cp -r godot-refactoring ~/.config/opencode/superpowers/skills/
```

#### Option C: Install Only Project Structure Skill

```bash
# Copy just the project structure organizer
cp project-structure-organizer/SKILL.md ~/.config/opencode/superpowers/skills/project-structure-organizer.md
```

### Step 3: Verify Installation

Restart Claude Code CLI and the skills will be available in your commands.

## How to Use

### In Claude Code CLI

Navigate to your Godot project folder:

```bash
cd /path/to/your/godot/project
claude
```

Then use the skills:

**For Refactoring:**
```
> Use godot-refactoring to analyze this Godot project

The skill will:
1. Detect anti-patterns
2. Suggest refactoring operations
3. Create git commits
4. Preserve behavior exactly
```

**For Project Structure:**
```
> Use project-structure-organizer to reorganize this project structure

The skill will:
1. Analyze current structure
2. Propose reorganization
3. Move files intelligently
4. Update all references
```

### In Claude.ai Web (With Claude Code Extension)

If you have Claude Code extension installed:
1. Create a new project in Claude Code
2. Upload your Godot project files
3. Use the same commands as above

### In OpenCode / Other Claude Code Variants

The skills work with any Claude Code-compatible environment:
1. Ensure `~/.config/opencode/superpowers/skills/` directory exists
2. Copy skill folders using the installation commands above
3. Restart your Claude Code environment
4. Skills will be available immediately

## Requirements

- **Claude Code CLI** - Download from [anthropics/claude-code](https://github.com/anthropics/claude-code)
- **Godot 4.x** - Download from [godotengine.org](https://godotengine.org/)
- **Git** for version control - Usually pre-installed on Linux/Mac, [download for Windows](https://git-scm.com/)
- Standard Unix tools (grep, find, awk) - Pre-installed on Linux/Mac, included in Git Bash on Windows

## Documentation

- [Godot Superpowers - Refactoring](./godot-refactoring/) - Complete skill documentation
- [Godot Superpowers - Project Structure](./project-structure-organizer/) - Complete skill documentation
- [Detailed Installation Guide](./INSTALLATION.md) - Step-by-step for all platforms
- [Contributing Guide](./CONTRIBUTING.md) - How to contribute
- [Changelog](./CHANGELOG.md) - Version history and updates

## Features Highlight

### Intelligent Node Selection
- 9 decision trees for automatic node type detection
- Confidence scoring (50-99%)
- Pattern matching on variables, properties, methods
- 80+ Godot node catalog

### Modular Component System
- Zero duplication architecture
- Automatic component library building
- Inspector-configurable presets
- Reusable base scenes

### Safety First
- Git baseline before changes
- Per-operation validation
- Automatic rollback on failure
- Iron Law: NO functional changes

## Examples & Guides

See detailed examples in:
- [Godot Superpowers - Refactoring Examples](./godot-refactoring/EXAMPLES.md)
- [Comprehensive Documentation](./godot-refactoring/docs/)
- [Complete Index & Navigation](./godot-refactoring/INDEX.md)

## Statistics

- **12,800+ lines** of comprehensive documentation
- **150+ Godot nodes** cataloged and documented
- **5 automatic operations** for automation
- **Production ready** and battle-tested
- **2 professional skills** included

## Quick Start Video

1. Clone the repository
2. Copy skills to `~/.config/opencode/superpowers/skills/`
3. Open your Godot project
4. Use `claude` command in terminal
5. Invoke Godot Superpowers skills

## License

MIT License - See [LICENSE](./LICENSE)

Godot is © Copyright 2014-present Juan Linietsky, Ariel Manzur and the Godot community.

## Contributing

Contributions welcome! See [CONTRIBUTING.md](./CONTRIBUTING.md)

## Created for the Godot Community

These skills are designed to help Godot developers maintain clean, modular projects with professional-grade automation. 💙

## Support & Issues

- 📋 [GitHub Issues](https://github.com/asreonn/godot-superpowers/issues) - Report bugs or suggest features
- 💬 [GitHub Discussions](https://github.com/asreonn/godot-superpowers/discussions) - Ask questions and discuss
- 📖 [Full Documentation](./godot-refactoring/) - Detailed guides and examples
