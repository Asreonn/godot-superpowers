# Godot Superpowers 🚀

Professional Godot project refactoring and organization skills for Claude Code CLI.

## What's Included

### 1. Godot Refactoring Skill
Automatically refactor Godot projects to clean, modular architecture with zero functional changes.

**Features:**
- Extract code-created nodes to modular components
- Intelligent node selection with 90%+ confidence
- Automatic component library building
- Split monolithic scripts
- Signal-based decoupling
- Data extraction to resources

[➡️ Read more](./godot-refactoring/)

### 2. Project Structure Organizer Skill
Scan and intelligently reorganize project folder structure for optimal organization.

**Features:**
- Automatic project structure analysis
- Smart file categorization
- Directory hierarchy creation
- Reference auto-updating
- Full rollback support

[➡️ Read more](./project-structure-organizer/)

## Installation

### Quick Install (Recommended)

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/godot-superpowers.git

# Install both skills
cd godot-superpowers

# Install godot-refactoring
cp -r godot-refactoring ~/.config/opencode/superpowers/skills/

# Install project-structure-organizer
cp project-structure-organizer/SKILL.md ~/.config/opencode/superpowers/skills/project-structure-organizer.md
```

### Individual Skill Installation

**Install just godot-refactoring:**
```bash
cp -r godot-refactoring ~/.config/opencode/superpowers/skills/
```

**Install just project-structure-organizer:**
```bash
cp project-structure-organizer/SKILL.md ~/.config/opencode/superpowers/skills/project-structure-organizer.md
```

[➡️ Detailed installation instructions](./INSTALLATION.md)

## Usage

### godot-refactoring
```
In your Godot project directory:
> Refactor this Godot project using godot-refactoring skill

The skill will automatically:
1. Detect anti-patterns
2. Refactor to clean architecture
3. Create git commits
4. Preserve behavior exactly
```

### project-structure-organizer
```
In your Godot project directory:
> Reorganize project structure using project-structure-organizer skill

The skill will:
1. Analyze current structure
2. Propose reorganization
3. Move files intelligently
4. Update all references
```

## Requirements

- **Claude Code CLI** (Superpowers framework)
- **Godot 4.x** projects
- **Git** for version control
- Standard Unix tools (grep, find, awk)

## Documentation

- [Installation Guide](./INSTALLATION.md)
- [Godot Refactoring Docs](./godot-refactoring/)
- [Project Organizer Docs](./project-structure-organizer/)
- [Contributing](./CONTRIBUTING.md)
- [Changelog](./CHANGELOG.md)

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

## Examples

See detailed examples in:
- [godot-refactoring/EXAMPLES.md](./godot-refactoring/EXAMPLES.md)
- [godot-refactoring/docs/](./godot-refactoring/docs/)

## Statistics

- **12,800+ lines** of comprehensive documentation
- **150+ Godot nodes** cataloged and documented
- **5 automatic operations** for refactoring
- **Production ready** and battle-tested

## License

MIT License - See [LICENSE](./LICENSE)

## Contributing

Contributions welcome! See [CONTRIBUTING.md](./CONTRIBUTING.md)

## Author

Created for the Godot community 💙

## Support

- [GitHub Issues](https://github.com/YOUR_USERNAME/godot-superpowers/issues)
- [Discussions](https://github.com/YOUR_USERNAME/godot-superpowers/discussions)
