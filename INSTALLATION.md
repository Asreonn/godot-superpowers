# Installation Guide

## Prerequisites

1. **Claude Code CLI** with Superpowers support
   - Install from: https://github.com/anthropics/claude-code

2. **Godot 4.x** (for using the skills)
   - Download from: https://godotengine.org/

3. **Git** (required by skills)
   ```bash
   git --version  # Verify installation
   ```

## Installation Methods

### Method 1: Quick Install (Both Skills)

```bash
# Clone repository
git clone https://github.com/YOUR_USERNAME/godot-superpowers.git
cd godot-superpowers

# Create skills directory if it doesn't exist
mkdir -p ~/.config/opencode/superpowers/skills

# Install godot-refactoring
cp -r godot-refactoring ~/.config/opencode/superpowers/skills/

# Install project-structure-organizer
cp project-structure-organizer/SKILL.md ~/.config/opencode/superpowers/skills/project-structure-organizer.md

# Verify installation
ls -la ~/.config/opencode/superpowers/skills/
```

### Method 2: Individual Skill Installation

**Install only godot-refactoring:**
```bash
cd godot-superpowers
cp -r godot-refactoring ~/.config/opencode/superpowers/skills/
```

**Install only project-structure-organizer:**
```bash
cd godot-superpowers
cp project-structure-organizer/SKILL.md ~/.config/opencode/superpowers/skills/project-structure-organizer.md
```

### Method 3: Manual Installation

1. Navigate to skills directory:
   ```bash
   cd ~/.config/opencode/superpowers/skills
   ```

2. Create directory for godot-refactoring:
   ```bash
   mkdir -p godot-refactoring
   ```

3. Copy files manually from this repository

## Verification

### Verify godot-refactoring installation:

```bash
# Run validation script
bash ~/.config/opencode/superpowers/skills/godot-refactoring/validate-skill.sh
```

Expected output:
```
✓ godot-refactoring skill installed correctly
✓ All 15 files present
✓ YAML frontmatter valid
✓ Total: 12,220+ lines
```

### Verify project-structure-organizer installation:

```bash
# Check file exists
ls -lh ~/.config/opencode/superpowers/skills/project-structure-organizer.md
```

### Test in Claude Code:

```bash
# Navigate to a Godot project
cd /path/to/your/godot/project

# Start Claude Code
claude

# Try invoking the skill
> Use godot-refactoring skill to analyze this project
```

## Updating

```bash
cd godot-superpowers
git pull origin main

# Reinstall (overwrites existing)
cp -r godot-refactoring ~/.config/opencode/superpowers/skills/
cp project-structure-organizer/SKILL.md ~/.config/opencode/superpowers/skills/project-structure-organizer.md
```

## Uninstallation

```bash
# Remove godot-refactoring
rm -rf ~/.config/opencode/superpowers/skills/godot-refactoring

# Remove project-structure-organizer
rm ~/.config/opencode/superpowers/skills/project-structure-organizer.md
```

## Troubleshooting

### Skill not detected

**Problem:** Claude Code doesn't recognize the skill

**Solution:**
1. Check file location:
   ```bash
   ls ~/.config/opencode/superpowers/skills/godot-refactoring/SKILL.md
   ```

2. Verify YAML frontmatter in SKILL.md:
   ```yaml
   ---
   name: godot-refactoring
   description: ...
   ---
   ```

3. Restart Claude Code CLI

### Validation script fails

**Problem:** `validate-skill.sh` reports errors

**Solution:**
1. Ensure all files are present
2. Check file permissions:
   ```bash
   chmod +x ~/.config/opencode/superpowers/skills/godot-refactoring/validate-skill.sh
   ```

### Permission denied

**Problem:** Cannot copy files

**Solution:**
```bash
# Ensure target directory exists
mkdir -p ~/.config/opencode/superpowers/skills

# Check permissions
ls -la ~/.config/opencode/superpowers/
```

## Next Steps

After installation:
1. Read [godot-refactoring/README.md](./godot-refactoring/README.md)
2. Try examples from [godot-refactoring/EXAMPLES.md](./godot-refactoring/EXAMPLES.md)
3. Review [godot-refactoring/INDEX.md](./godot-refactoring/INDEX.md) for navigation

## Support

- [GitHub Issues](https://github.com/YOUR_USERNAME/godot-superpowers/issues)
- [Discussions](https://github.com/YOUR_USERNAME/godot-superpowers/discussions)
