# Contributing to Godot Superpowers

Thank you for considering contributing! 🎉

## How to Contribute

### Reporting Bugs

1. Check [existing issues](https://github.com/YOUR_USERNAME/godot-superpowers/issues)
2. Create a new issue with:
   - Clear title
   - Steps to reproduce
   - Expected vs actual behavior
   - Godot version, OS, Claude Code version

### Suggesting Enhancements

1. Check [discussions](https://github.com/YOUR_USERNAME/godot-superpowers/discussions)
2. Create a new discussion or issue with:
   - Clear description of enhancement
   - Use case/motivation
   - Example implementation (if applicable)

### Pull Requests

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Make your changes
4. Test thoroughly
5. Commit: `git commit -m "Add amazing feature"`
6. Push: `git push origin feature/amazing-feature`
7. Open a Pull Request

#### PR Guidelines

- Follow existing code style
- Update documentation
- Add examples if applicable
- Ensure validate-skill.sh passes
- One feature per PR

### Documentation Improvements

Documentation improvements are always welcome!

- Fix typos
- Clarify explanations
- Add examples
- Improve navigation

### Testing

Before submitting:

```bash
# Validate godot-refactoring skill
bash godot-refactoring/validate-skill.sh

# Test on real Godot project
# Verify behavior unchanged
```

## Development Setup

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/godot-superpowers.git
cd godot-superpowers

# Install locally for testing
cp -r godot-refactoring ~/.config/opencode/superpowers/skills/
cp project-structure-organizer/SKILL.md ~/.config/opencode/superpowers/skills/project-structure-organizer.md
```

## Code of Conduct

- Be respectful
- Be constructive
- Be collaborative

## Questions?

- [GitHub Discussions](https://github.com/YOUR_USERNAME/godot-superpowers/discussions)
- [GitHub Issues](https://github.com/YOUR_USERNAME/godot-superpowers/issues)

Thank you! 💙
