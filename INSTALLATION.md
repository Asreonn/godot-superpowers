# Installation Guide - Godot Superpowers

Complete step-by-step installation instructions for all platforms and tools.

## Prerequisites

Before installing Godot Superpowers, ensure you have:

1. **Claude Code CLI** - The command-line interface for Claude
   - Download: https://github.com/anthropics/claude-code
   - Verify: `claude --version`

2. **Godot 4.x** - Game engine (you'll use the skills on Godot projects)
   - Download: https://godotengine.org/
   - Verify: `godot --version`

3. **Git** - Version control system
   - Linux: `sudo apt install git` (Ubuntu/Debian) or your package manager
   - Mac: Usually pre-installed, or `brew install git`
   - Windows: https://git-scm.com/download/win

## Installation - Linux & Mac

### Step 1: Clone the Repository

```bash
# Clone to your preferred location
git clone https://github.com/asreonn/godot-superpowers.git
cd godot-superpowers
```

### Step 2: Ensure Skills Directory Exists

```bash
# Create the superpowers skills directory
mkdir -p ~/.config/opencode/superpowers/skills
```

### Step 3: Install Godot Superpowers

**Option A: Install Both Skills (Recommended)**

```bash
# Copy both skills
cp -r godot-refactoring ~/.config/opencode/superpowers/skills/
cp project-structure-organizer/SKILL.md ~/.config/opencode/superpowers/skills/project-structure-organizer.md

# Verify
ls -la ~/.config/opencode/superpowers/skills/
```

**Option B: Install Only Refactoring**

```bash
cp -r godot-refactoring ~/.config/opencode/superpowers/skills/
```

**Option C: Install Only Project Structure Organizer**

```bash
cp project-structure-organizer/SKILL.md ~/.config/opencode/superpowers/skills/project-structure-organizer.md
```

### Step 4: Verify Installation

```bash
# Check if godot-refactoring is installed
bash ~/.config/opencode/superpowers/skills/godot-refactoring/validate-skill.sh \
  ~/.config/opencode/superpowers/skills/godot-refactoring

# You should see:
# ✓ Skill validation PASSED
# The godot-refactoring skill is ready to use!
```

### Step 5: Test in Claude Code

```bash
# Navigate to any Godot project
cd /path/to/your/godot/project

# Start Claude Code
claude

# Then in Claude Code interface, type:
# > Use godot-refactoring to analyze this Godot project
```

## Installation - Windows

### Step 1: Clone the Repository

Open Command Prompt or PowerShell:

```cmd
git clone https://github.com/asreonn/godot-superpowers.git
cd godot-superpowers
```

### Step 2: Find Your Skills Directory

```cmd
# Create the directory if it doesn't exist
mkdir %USERPROFILE%\.config\opencode\superpowers\skills
```

### Step 3: Copy Skills

**Option A: Using PowerShell (Recommended)**

```powershell
# Copy both skills
Copy-Item -Recurse "godot-refactoring" -Destination "$env:USERPROFILE\.config\opencode\superpowers\skills\"
Copy-Item "project-structure-organizer\SKILL.md" -Destination "$env:USERPROFILE\.config\opencode\superpowers\skills\project-structure-organizer.md"

# Verify
Get-ChildItem "$env:USERPROFILE\.config\opencode\superpowers\skills\"
```

**Option B: Using File Explorer**

1. Open the cloned `godot-superpowers` folder
2. Navigate to `User → .config → opencode → superpowers → skills` in File Explorer
3. Copy `godot-refactoring` folder into the skills directory
4. Copy `project-structure-organizer/SKILL.md` to the skills directory

### Step 4: Test Installation

```cmd
# Open Command Prompt and go to a Godot project
cd C:\path\to\your\godot\project

# Start Claude Code
claude

# Then type:
# > Use godot-refactoring to analyze this Godot project
```

## Installation - Using Claude.ai Web

If you use Claude at https://claude.ai/ with the Claude Code extension:

### Step 1: Install Claude Code Extension

1. Go to https://claude.ai/
2. Install the Claude Code browser extension (if not already installed)

### Step 2: Install Godot Superpowers from Terminal

Open the Claude Code terminal in the web interface:

```bash
# Clone repository
git clone https://github.com/asreonn/godot-superpowers.git
cd godot-superpowers

# Install skills
mkdir -p ~/.config/opencode/superpowers/skills
cp -r godot-refactoring ~/.config/opencode/superpowers/skills/
cp project-structure-organizer/SKILL.md ~/.config/opencode/superpowers/skills/project-structure-organizer.md
```

### Step 3: Create New Claude Code Project

1. In Claude.ai, create a new Claude Code project
2. Upload your Godot project files
3. Use the same commands as in Claude Code CLI

## Installation - Using OpenCode

If you use OpenCode or other Claude Code variants:

The installation is identical to Linux/Mac:

```bash
# Clone and install
git clone https://github.com/asreonn/godot-superpowers.git
cd godot-superpowers

mkdir -p ~/.config/opencode/superpowers/skills
cp -r godot-refactoring ~/.config/opencode/superpowers/skills/
cp project-structure-organizer/SKILL.md ~/.config/opencode/superpowers/skills/project-structure-organizer.md
```

Restart OpenCode and the skills will be available.

## Troubleshooting

### Issue: "Skill not found" error

**Solution:**
1. Check if skills directory exists: `ls ~/.config/opencode/superpowers/skills/`
2. Check if files were copied correctly
3. Restart Claude Code: `claude`
4. Verify SKILL.md has correct frontmatter:
   ```bash
   head -3 ~/.config/opencode/superpowers/skills/godot-refactoring/SKILL.md
   # Should show: ---
   #             name: godot-refactoring
   ```

### Issue: "Permission denied" when copying files

**Solution:**
```bash
# Ensure proper permissions
chmod -R 755 ~/.config/opencode/superpowers/skills/
```

### Issue: "validate-skill.sh: command not found" on Windows

**Solution:**
Windows doesn't have bash by default. Install:
- Git Bash: https://git-scm.com/ (includes bash)
- WSL (Windows Subsystem for Linux): https://docs.microsoft.com/en-us/windows/wsl/

Or just verify manually:
```bash
ls ~/.config/opencode/superpowers/skills/godot-refactoring/SKILL.md
# If file exists, installation is complete
```

## Updating to New Versions

When new versions of Godot Superpowers are released:

```bash
# Go to your cloned repository
cd path/to/godot-superpowers

# Get the latest version
git pull origin main

# Reinstall (overwrites previous version)
cp -r godot-refactoring ~/.config/opencode/superpowers/skills/
cp project-structure-organizer/SKILL.md ~/.config/opencode/superpowers/skills/project-structure-organizer.md
```

## Uninstalling

### Remove Everything

```bash
# Remove godot-refactoring
rm -rf ~/.config/opencode/superpowers/skills/godot-refactoring

# Remove project-structure-organizer
rm ~/.config/opencode/superpowers/skills/project-structure-organizer.md
```

### Remove Just One Skill

```bash
# Remove only refactoring
rm -rf ~/.config/opencode/superpowers/skills/godot-refactoring

# OR remove only organizer
rm ~/.config/opencode/superpowers/skills/project-structure-organizer.md
```

## Next Steps

1. **Read the Documentation**
   - [Godot Superpowers - Refactoring Guide](./godot-refactoring/)
   - [Godot Superpowers - Project Structure Guide](./project-structure-organizer/)

2. **Try the Examples**
   - Look at [EXAMPLES.md](./godot-refactoring/EXAMPLES.md)
   - See real-world usage scenarios

3. **Use on Your Project**
   ```bash
   cd /path/to/your/godot/project
   claude

   # Type:
   # > Use godot-refactoring to analyze this Godot project
   ```

## Support

- 📖 [Full Documentation](./godot-refactoring/)
- 💬 [GitHub Discussions](https://github.com/asreonn/godot-superpowers/discussions)
- 🐛 [Report Issues](https://github.com/asreonn/godot-superpowers/issues)

---

**Happy coding with Godot Superpowers!** 🚀
