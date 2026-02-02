# Changelog

All notable changes to Godot Superpowers will be documented in this file.

## [Unreleased]

- Scene Hierarchy Cleaner skill (planned)
- Scene Layout Organizer skill (planned)
- Additional documentation examples

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
