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

### 3. Godot Superpowers - Editor Position Sync
Fix position conflicts between Godot editor (.tscn) and code (.gd) - make editor preview match runtime.

**Features:**
- Detect position conflicts (editor vs code)
- Intelligent classification (intentional vs conflict)
- Camera-aware positioning for backgrounds
- Parallax layer handling
- Three sync strategies (Code→Editor, Editor→Code, Camera-Aware)
- Special handling for camera-following elements

[➡️ Read more](./editor-position-sync/)

## Installation

### Step 1: Clone This Repository

```bash
git clone https://github.com/asreonn/godot-superpowers.git
cd godot-superpowers
```

### Step 2: Install Godot Superpowers Skills

Choose your installation method below:

#### Option A: Install All Skills

```bash
# Copy all skills to your Claude Code skills directory
cp -r godot-refactoring ~/.config/opencode/superpowers/skills/
cp -r editor-position-sync ~/.config/opencode/superpowers/skills/
cp project-structure-organizer/SKILL.md ~/.config/opencode/superpowers/skills/project-structure-organizer.md
```

#### Option B: Install Individual Skills

```bash
# Refactoring skill only
cp -r godot-refactoring ~/.config/opencode/superpowers/skills/

# Editor Position Sync only
cp -r editor-position-sync ~/.config/opencode/superpowers/skills/

# Project Structure only
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

**For Editor Position Sync:**
```
> My background follows the camera but appears at (0,0) in the editor

The skill will:
1. Detect position conflicts
2. Classify as camera-following
3. Sync editor position to camera start
4. Document camera-relative behavior
5. Make editor preview accurate
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
- [Godot Superpowers - Editor Position Sync](./editor-position-sync/) - Complete skill documentation
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

- **15,000+ lines** of comprehensive documentation
- **150+ Godot nodes** cataloged and documented
- **8 automatic operations** for automation (5 refactoring + 3 sync strategies)
- **Production ready** and battle-tested
- **3 professional skills** included

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
