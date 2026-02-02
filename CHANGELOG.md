# Changelog

All notable changes to Godot Superpowers will be documented in this file.

## [Unreleased]

- Scene Hierarchy Cleaner skill (planned)
- Scene Layout Organizer skill (planned)
- Additional documentation examples

## [3.0.0] - 2026-02-02

### Breaking Changes

**Skill Names Changed:**
- `godot-refactoring` → `godot-refactor`
- `project-structure-organizer` → `godot-organize-project`
- `editor-position-sync` → `godot-fix-positions`

**Directory Structure Changed:**
- Skills moved to `orchestrators/` directory
- New `mini-skills/` directory added

**Installation Paths Changed:**
- Old: Install from root directory
- New: Install from `orchestrators/` or `mini-skills/` directories

See [MIGRATION.md](./MIGRATION.md) for migration guide.

### Added - Mini-Skills Architecture

**11 New Mini-Skills for Granular Operations:**

**Code Quality Mini-Skills (5):**
- `godot-extract-to-scenes` - Extract code-created objects to .tscn files
- `godot-split-scripts` - Split monolithic scripts over 150 lines
- `godot-add-signals` - Replace get_node coupling with signals
- `godot-extract-resources` - Move const data to .tres resources
- `godot-clean-conflicts` - Remove conflicting operations

**Organization Mini-Skills (3):**
- `godot-organize-files` - Organize project folder structure
- `godot-organize-assets` - Organize assets by type
- `godot-organize-scripts` - Organize scripts by category

**Position Sync Mini-Skills (3):**
- `godot-sync-static-positions` - Fix static position conflicts
- `godot-sync-camera-positions` - Camera-aware background positioning
- `godot-sync-parallax` - Parallax layer editor preview sync

**3 Orchestrator Skills:**
- `godot-refactor` - Orchestrates all 5 code quality mini-skills
- `godot-organize-project` - Orchestrates all 3 organization mini-skills
- `godot-fix-positions` - Orchestrates all 3 position sync mini-skills

### Enhanced

**Skill Frontmatter:**
- Added `summary` - One-line description for quick understanding
- Enhanced `description` with detailed use cases
- Added `use_cases` - List of problem statements agents can match
- Added `outputs` - What files/changes the skill produces
- Added `requirements` - Git, Godot version, tools needed
- Added `execution` - Automation level and user interaction
- Added `auto_rollback` - Safety features documented
- Added `integration` - Compatible skills and workflows

**Documentation:**
- Complete rewrite of README.md for v3.0 structure
- New MIGRATION.md guide for v2.x → v3.0 users
- Each mini-skill has comprehensive SKILL.md documentation
- Updated installation instructions for new structure

**Agent Discoverability:**
- Mini-skills are easier for agents to discover by problem description
- Clear use_cases help agents choose correct skill
- Focused skill names indicate purpose (extract, split, sync, etc.)

### Features

**Modular Architecture:**
- Run individual mini-skills for specific operations
- Run orchestrators for full workflows
- Mix and match based on needs
- Clear separation of concerns

**Backwards Compatible Workflows:**
- Orchestrators maintain v2.x behavior
- Same automatic analysis and operations
- Same git commits and rollback
- Users can upgrade without workflow changes

**Flexibility:**
- Install only what you need (mini-skills, orchestrators, or both)
- Granular control over operations
- Faster execution for single operations
- Choose between comprehensive or targeted refactoring

### Statistics

- **14 total skills** (11 mini-skills + 3 orchestrators)
- **15,000+ lines** of comprehensive documentation
- **Enhanced frontmatter** on all skills
- **3 installation options** (orchestrators only, mini-skills only, or both)

## [2.0.0] - 2026-02-02

### Added - Editor Position Sync Skill
- **NEW SKILL**: Editor Position Sync - Fix position conflicts between editor (.tscn) and code (.gd)
- Intelligent position conflict detection
- Camera-aware positioning for backgrounds and parallax layers
- Three sync strategies: CODE_TO_EDITOR, EDITOR_TO_CODE, CAMERA_AWARE
- Automatic classification: CONFLICT, INTENTIONAL_DYNAMIC, INTENTIONAL_ANIMATION, PROCESS_ASSIGNMENT
- Camera start position detection from main scene
- Special handling for parallax backgrounds
- Documentation for camera-following elements
- Automatic validation and rollback on errors
- Git commits per sync operation

### Enhanced
- Updated README with third skill documentation
- Added installation instructions for editor-position-sync
- Updated statistics (3 skills, 15,000+ lines of documentation)
- Complete documentation set for editor-position-sync

## [1.0.0] - 2026-02-02

### Added

#### godot-refactoring skill
- Initial release with 5 automatic refactoring operations
- Intelligent node selection with 9 decision trees
- Comprehensive Godot 4.x node catalog (80+ nodes documented)
- Modular component library system with zero duplication
- Confidence scoring system (50-99%) for node selection
- Automatic component library building
- Scene reusability patterns with preset resources
- Complete documentation (12,220+ lines)
- Validation script for skill integrity

**Operations:**
- Operation A: Extract code-created objects to modular components
- Operation B: Split monolithic scripts
- Operation C: Signal-based decoupling
- Operation D: Extract data to resources
- Operation E: Clean conflicting operations

**Documentation:**
- godot-node-reference.md (4,200+ lines)
- node-selection-guide.md (1,100+ lines)
- scene-reusability-patterns.md (900+ lines)
- refactoring-operations.md (1,100 lines)
- EXAMPLES.md with 6 detailed examples
- INDEX.md for navigation
- And 8 more supporting docs

#### project-structure-organizer skill
- Initial release
- Automatic project structure analysis
- Smart file categorization and organization
- Directory hierarchy creation
- Reference auto-updating
- Full rollback support via git
- Integration with godot-refactoring skill

### Features
- Git safety baseline before all changes
- Per-operation validation testing
- Automatic rollback on test failure
- Iron Law: NO functional or visual changes guaranteed
- Component library auto-organization
- Inspector-configurable presets

## Version History

### v1.0.0 (2026-02-02)
Initial public release

---

## Format

Based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)

Versioning: [Semantic Versioning](https://semver.org/)
