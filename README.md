# Godot Superpowers 🚀

Professional-grade Godot 4.x automation skills for AI coding assistants (Claude Code, OpenCode, Codex).

**Version 4.0.0** - Production-ready with full Godot 4.x support! 🎉

---

## ✨ What's New in v4.0

**29 Total Skills** (up from 14 in v3.0)

### 🆕 15 New Godot 4.x Skills

**Critical Priority (P0):**
- `godot-modernize-gdscript` - GDScript 1.0 → 2.0 migration
- `godot-migrate-tilemap` - TileMap → TileMapLayer (Godot 4.3+)

**High Priority (P1):**
- `godot-profile-performance` - Performance bottleneck detection
- `godot-generate-tests` - GUT test generation
- `godot-setup-navigation` - NavigationServer setup
- `godot-setup-multiplayer` - New multiplayer API setup
- `godot-optimize-rendering` - Rendering optimization
- `godot-setup-animationtree` - AnimationTree state machines

**Medium Priority (P2):**
- `godot-convert-shaders` - Shader conversion (3.x → 4.x)
- `godot-setup-csharp` - C# integration
- `godot-modernize-ui` - UI modernization
- `godot-setup-audio-buses` - Audio bus architecture
- `godot-setup-export` - Multi-platform exports

**Low Priority (P3):**
- `godot-modernize-input` - Input system modernization
- `godot-create-plugin` - Editor plugin creation

---

## 📦 Quick Install

```bash
# Clone the repository
git clone https://github.com/asreonn/godot-superpowers.git
cd godot-superpowers

# Install for Claude Code
cp -r mini-skills/* orchestrators/* ~/.claude/skills/

# Install for OpenCode
cp -r mini-skills/* orchestrators/* ~/.config/opencode/skills/

# Install for Codex CLI
cp -r mini-skills/* orchestrators/* ~/.codex/skills/
```

---

## 📋 All 29 Skills

### 🎛️ Orchestrators (3)
High-level coordination skills that run multiple mini-skills:

1. **`godot-refactor`** - Comprehensive code quality refactoring
   - Orchestrates: extract-to-scenes, split-scripts, add-signals, extract-resources, clean-conflicts

2. **`godot-organize-project`** - Project structure organization
   - Orchestrates: organize-files, organize-assets, organize-scripts

3. **`godot-fix-positions`** - Editor/code position synchronization
   - Orchestrates: sync-static-positions, sync-camera-positions, sync-parallax

### 🔧 Core Godot 4.x Skills (15)

**Migration & Modernization:**
- `godot-modernize-gdscript` - Convert yield→await, onready→@onready, export→@export
- `godot-migrate-tilemap` - Migrate to TileMapLayer system (Godot 4.3+)
- `godot-convert-shaders` - Convert Godot 3.x shaders to 4.x
- `godot-modernize-ui` - Modernize UI to Godot 4.x best practices
- `godot-modernize-input` - Modernize input handling

**Performance & Quality:**
- `godot-profile-performance` - Detect bottlenecks in _process, get_node() loops
- `godot-optimize-rendering` - Optimize Forward+/Mobile/Compatibility renderers
- `godot-generate-tests` - Generate GUT unit tests

**System Setup:**
- `godot-setup-navigation` - Setup NavigationServer with pathfinding
- `godot-setup-multiplayer` - Setup MultiplayerSpawner, RPC, authority
- `godot-setup-animationtree` - Setup AnimationTree state machines
- `godot-setup-audio-buses` - Setup Master/Music/SFX bus architecture
- `godot-setup-csharp` - Setup C# integration
- `godot-setup-export` - Setup multi-platform exports
- `godot-create-plugin` - Create Godot Editor plugins

### 🛠️ Original Mini-Skills (11)

**Code Quality:**
- `godot-extract-to-scenes` - Convert Timer.new() to .tscn files
- `godot-split-scripts` - Split monolithic scripts >150 lines
- `godot-add-signals` - Replace get_node() with signals
- `godot-extract-resources` - Move const data to .tres files
- `godot-clean-conflicts` - Clean position conflicts, duplicate signals

**Organization:**
- `godot-organize-files` - Organize project folder structure
- `godot-organize-assets` - Organize assets by type
- `godot-organize-scripts` - Organize scripts by category

**Position Sync:**
- `godot-sync-static-positions` - Fix editor vs _ready() positions
- `godot-sync-camera-positions` - Camera-aware positioning
- `godot-sync-parallax` - Parallax layer sync

---

## 🎯 Use Cases

### Godot 3.x → 4.x Migration
```
1. godot-modernize-gdscript    # Update syntax
2. godot-migrate-tilemap       # Update TileMap (4.3+)
3. godot-convert-shaders       # Update shaders
4. godot-modernize-ui          # Update UI
5. godot-setup-multiplayer     # Update networking
```

### Performance Optimization
```
1. godot-profile-performance   # Find bottlenecks
2. godot-optimize-rendering    # Optimize rendering
```

### New Project Setup
```
1. godot-organize-project      # Organize structure
2. godot-setup-navigation      # Add pathfinding
3. godot-setup-audio-buses     # Setup audio
4. godot-setup-export          # Configure exports
```

---

## 🚀 How to Use

### Example: Modernize GDScript
```
User: "Convert my Godot 3.x code to 4.x"
AI: Invokes godot-modernize-gdscript
Result: yield→await, onready→@onready, export→@export, etc.
```

### Example: Full Refactor
```
User: "Clean up my entire project"
AI: Invokes godot-refactor orchestrator
Result: All 5 code quality operations run automatically
```

### Example: Setup Navigation
```
User: "Add pathfinding to my game"
AI: Invokes godot-setup-navigation
Result: NavigationRegion2D, NavigationAgent setup
```

---

## ✅ Requirements

- **Godot 4.0+** (4.3+ for TileMap V2)
- **Git** repository initialized
- **AI Assistant:** Claude Code, OpenCode, or Codex CLI
- **Bash/Shell** environment

---

## 📊 Statistics

| Metric | Value |
|--------|-------|
| Total Skills | **29** |
| Orchestrators | 3 |
| Mini-Skills | 26 |
| Godot 4.x Skills | 15 |
| Lines of Documentation | 25,000+ |
| Validation Pass Rate | 100% |

---

## 📚 Documentation

- [Release Notes](./RELEASE_NOTES.md) - v4.0.0 release details
- [Changelog](./CHANGELOG.md) - Version history
- [Vision & Strategy](./docs/01_VISION_AND_STRATEGY.md) - Project roadmap
- [Godot 4.x Requirements](./docs/02_GODOT4_REQUIREMENTS.md) - Feature specs
- [Implementation Roadmap](./docs/03_IMPLEMENTATION_ROADMAP.md) - Detailed plan
- [AGENTS.md](./AGENTS.md) - AI agent instructions

---

## 🏗️ Infrastructure

- ✅ GitHub Actions CI/CD pipeline
- ✅ SKILL.md v2.0 validation scripts
- ✅ Test framework (pytest)
- ✅ Cross-platform support (Windows, macOS, Linux)

---

## 🔧 Validation

```bash
# Check all skills
python scripts/validate_skills.py

# Check frontmatter
python scripts/check_frontmatter.py

# Run tests
pytest tests/ -v
```

---

## 🤝 Contributing

Contributions welcome! All skills follow SKILL.md v2.0 format with:
- YAML frontmatter
- Before/after examples
- Validation tests
- Clear documentation

---

## 📜 License

MIT License - See [LICENSE](./LICENSE)

Godot is © Copyright 2014-present Juan Linietsky, Ariel Manzur and the Godot community.

---

## 💙 Created for the Godot Community

These skills automate tedious Godot development tasks while maintaining clean, professional-grade code quality.

**Happy Game Development! 🎮**
