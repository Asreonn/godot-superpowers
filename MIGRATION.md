# Migration Guide: v2.x → v3.0

This guide helps you migrate from Godot Superpowers v2.x to v3.0.

## What Changed in v3.0

### Breaking Changes

1. **Skill Names Changed**
   - `godot-refactoring` → `godot-refactor`
   - `project-structure-organizer` → `godot-organize-project`
   - `editor-position-sync` → `godot-fix-positions`

2. **Directory Structure Changed**
   - Skills moved to `orchestrators/` directory
   - New `mini-skills/` directory added with 11 mini-skills

3. **Installation Paths Changed**
   - Old: `godot-refactoring/`, `project-structure-organizer/`, `editor-position-sync/`
   - New: `orchestrators/godot-refactor/`, `orchestrators/godot-organize-project/`, `orchestrators/godot-fix-positions/`

### Non-Breaking Additions

- 11 new mini-skills for granular operations
- Enhanced frontmatter with use_cases, outputs, requirements
- Better agent discoverability

## Migration Steps

### Step 1: Backup Current Installation

```bash
# Backup your current skills
cd ~/.config/opencode/superpowers/skills/
mkdir -p ~/godot-superpowers-backup
cp -r godot-refactoring ~/godot-superpowers-backup/ 2>/dev/null || true
cp -r project-structure-organizer ~/godot-superpowers-backup/ 2>/dev/null || true
cp -r editor-position-sync ~/godot-superpowers-backup/ 2>/dev/null || true
```

### Step 2: Remove Old Skills

```bash
# Remove old skill directories
rm -rf ~/.config/opencode/superpowers/skills/godot-refactoring
rm -rf ~/.config/opencode/superpowers/skills/project-structure-organizer
rm -rf ~/.config/opencode/superpowers/skills/editor-position-sync

# Or remove individual SKILL.md files if you installed that way
rm ~/.config/opencode/superpowers/skills/godot-refactoring.md 2>/dev/null || true
rm ~/.config/opencode/superpowers/skills/project-structure-organizer.md 2>/dev/null || true
rm ~/.config/opencode/superpowers/skills/editor-position-sync.md 2>/dev/null || true
```

### Step 3: Install v3.0 Skills

Choose your installation method:

#### Option A: Install Everything (Recommended)

```bash
cd /path/to/godot-superpowers
git pull origin main

# Install all mini-skills
cp -r mini-skills/* ~/.config/opencode/superpowers/skills/

# Install all orchestrators
cp -r orchestrators/* ~/.config/opencode/superpowers/skills/
```

#### Option B: Install Only Orchestrators

If you want to keep the same workflow as v2.x (full refactoring):

```bash
cd /path/to/godot-superpowers
git pull origin main

# Install orchestrators only
cp -r orchestrators/* ~/.config/opencode/superpowers/skills/
```

#### Option C: Install Only Mini-Skills

If you want granular control and individual operations:

```bash
cd /path/to/godot-superpowers
git pull origin main

# Install mini-skills only
cp -r mini-skills/* ~/.config/opencode/superpowers/skills/
```

### Step 4: Verify Installation

```bash
# List installed skills
ls ~/.config/opencode/superpowers/skills/

# Should see:
# - godot-refactor/ (if orchestrators installed)
# - godot-organize-project/ (if orchestrators installed)
# - godot-fix-positions/ (if orchestrators installed)
# - godot-extract-to-scenes/ (if mini-skills installed)
# - godot-split-scripts/ (if mini-skills installed)
# - ... (9 more mini-skills)
```

### Step 5: Restart Claude Code

```bash
# Restart Claude Code CLI to load new skills
exit
claude
```

## Skill Name Mapping

| v2.x Name | v3.0 Orchestrator | v3.0 Mini-Skills |
|-----------|-------------------|------------------|
| `godot-refactoring` | `godot-refactor` | `godot-extract-to-scenes`<br>`godot-split-scripts`<br>`godot-add-signals`<br>`godot-extract-resources`<br>`godot-clean-conflicts` |
| `project-structure-organizer` | `godot-organize-project` | `godot-organize-files`<br>`godot-organize-assets`<br>`godot-organize-scripts` |
| `editor-position-sync` | `godot-fix-positions` | `godot-sync-static-positions`<br>`godot-sync-camera-positions`<br>`godot-sync-parallax` |

## Usage Changes

### Before (v2.x)

```
> Use godot-refactoring to analyze this project

Result: Runs all 5 refactoring operations
```

### After (v3.0) - Same Workflow

```
> Use godot-refactor to analyze this project

Result: Runs all 5 refactoring operations (same behavior)
```

### After (v3.0) - New Granular Workflow

```
> I have code that creates timers with Timer.new()

Result: Claude invokes godot-extract-to-scenes only (new!)
```

## Benefits of v3.0

### More Control

**v2.x:** Run full refactoring or nothing.

**v3.0:** Run individual operations or full refactoring.

```
# v2.x - Must run all operations
> Use godot-refactoring

# v3.0 - Run specific operation
> Use godot-extract-to-scenes
```

### Better Agent Discovery

**v2.x:** Agent must know exact skill name.

**v3.0:** Agent can discover skills by problem description.

```
User: "My code creates objects with .new()"
Agent: Searches use_cases, finds godot-extract-to-scenes
```

### Clearer Purpose

**v2.x:** "godot-refactoring" - What does it do?

**v3.0:** "godot-extract-to-scenes" - Clear purpose!

## Backwards Compatibility

### Orchestrators Maintain v2.x Behavior

The new orchestrator skills (`godot-refactor`, etc.) maintain the same workflow as v2.x:

- Same automatic analysis
- Same 5/3/3 operations in sequence
- Same git commits per operation
- Same rollback behavior

**You can use v3.0 orchestrators exactly like v2.x skills.**

### Recommended Approach

1. **Install both orchestrators and mini-skills**
2. **Use orchestrators for full workflows** (like v2.x)
3. **Use mini-skills for specific problems** (new in v3.0)

Best of both worlds!

## Common Migration Issues

### Issue 1: Skill Not Found

**Problem:** `godot-refactoring` skill not found after migration.

**Solution:** Use new name `godot-refactor` or install orchestrators.

```bash
# Install orchestrators
cp -r orchestrators/godot-refactor ~/.config/opencode/superpowers/skills/
```

### Issue 2: Want Old Behavior

**Problem:** Prefer simple "refactor everything" workflow.

**Solution:** Install only orchestrators, ignore mini-skills.

```bash
# Install orchestrators only (simple workflow)
cp -r orchestrators/* ~/.config/opencode/superpowers/skills/
```

### Issue 3: Too Many Skills

**Problem:** 14 total skills (11 mini + 3 orchestrators) is overwhelming.

**Solution:** Install based on your workflow preference.

```bash
# Minimalist: Orchestrators only (3 skills)
cp -r orchestrators/* ~/.config/opencode/superpowers/skills/

# Maximalist: Everything (14 skills)
cp -r orchestrators/* mini-skills/* ~/.config/opencode/superpowers/skills/

# Granular: Mini-skills only (11 skills)
cp -r mini-skills/* ~/.config/opencode/superpowers/skills/
```

## What You Get With Each Option

### Orchestrators Only (3 skills)

**Pros:**
- Simple workflow like v2.x
- Fewer skills to manage
- Full refactoring in one command

**Cons:**
- No granular control
- Must run all operations

**Best for:** Users who want comprehensive refactoring without complexity.

### Mini-Skills Only (11 skills)

**Pros:**
- Granular control
- Run only what you need
- Fast individual operations

**Cons:**
- More skills to learn
- Must know which skill to use

**Best for:** Users who want precise control and incremental refactoring.

### Both (14 skills)

**Pros:**
- Maximum flexibility
- Use orchestrators for full workflows
- Use mini-skills for specific problems

**Cons:**
- More skills installed

**Best for:** Most users - best of both worlds!

## Example Migration Scenarios

### Scenario 1: Simple User

**v2.x Usage:**
- Occasionally runs full refactoring
- Doesn't need granular control

**v3.0 Recommendation:**
```bash
# Install orchestrators only
cp -r orchestrators/* ~/.config/opencode/superpowers/skills/
```

**New Usage:** Same as before, just use `godot-refactor` instead of `godot-refactoring`.

### Scenario 2: Power User

**v2.x Usage:**
- Runs full refactoring occasionally
- Often needs specific operations only

**v3.0 Recommendation:**
```bash
# Install everything
cp -r orchestrators/* mini-skills/* ~/.config/opencode/superpowers/skills/
```

**New Usage:**
- Full refactoring: `godot-refactor` (orchestrator)
- Specific operation: `godot-extract-to-scenes` (mini-skill)

### Scenario 3: Team Lead

**v2.x Usage:**
- Uses refactoring on team projects
- Wants team members to use specific operations

**v3.0 Recommendation:**
```bash
# Install everything for flexibility
cp -r orchestrators/* mini-skills/* ~/.config/opencode/superpowers/skills/

# Document which skills to use when
cat > SKILLS_GUIDE.md <<EOF
Use godot-extract-to-scenes when adding new features
Use godot-split-scripts before code review
Use godot-refactor for legacy code cleanup
EOF
```

**New Usage:**
- Onboarding: Use orchestrators (simple)
- Daily dev: Use mini-skills (precise)

## Rollback to v2.x

If you need to rollback:

```bash
# Remove v3.0 skills
rm -rf ~/.config/opencode/superpowers/skills/godot-*

# Restore from backup
cp -r ~/godot-superpowers-backup/* ~/.config/opencode/superpowers/skills/

# Or reinstall v2.x from git
cd /path/to/godot-superpowers
git checkout v2.0.0
cp -r godot-refactoring ~/.config/opencode/superpowers/skills/
cp -r project-structure-organizer ~/.config/opencode/superpowers/skills/
cp -r editor-position-sync ~/.config/opencode/superpowers/skills/
```

## Questions?

- 📋 [GitHub Issues](https://github.com/asreonn/godot-superpowers/issues)
- 💬 [GitHub Discussions](https://github.com/asreonn/godot-superpowers/discussions)
- 📖 [README.md](./README.md) - Full v3.0 documentation

## Summary

**TL;DR:**

1. v3.0 renames skills and adds mini-skills
2. Install orchestrators for v2.x-like behavior
3. Install mini-skills for granular control
4. Install both for maximum flexibility
5. Orchestrators maintain v2.x workflow

**Recommended:** Install everything (orchestrators + mini-skills) for best experience.
