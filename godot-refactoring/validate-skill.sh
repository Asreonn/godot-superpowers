#!/bin/bash
# Validation script for godot-refactoring skill

SKILL_DIR="$HOME/.config/opencode/skills/godot-refactoring"
echo "Validating Godot Refactoring Skill..."
echo ""

# Check all required files exist
FILES=(
    "SKILL.md"
    "anti-patterns-detection.md"
    "tscn-generation-guide.md"
    "godot-best-practices.md"
    "refactoring-operations.md"
    "verification-checklist.md"
    "README.md"
)

echo "Checking required files..."
all_present=true
for file in "${FILES[@]}"; do
    if [ -f "$SKILL_DIR/$file" ]; then
        lines=$(wc -l < "$SKILL_DIR/$file")
        echo "  ✓ $file ($lines lines)"
    else
        echo "  ✗ $file MISSING"
        all_present=false
    fi
done
echo ""

# Check YAML frontmatter
echo "Checking YAML frontmatter..."
if head -5 "$SKILL_DIR/SKILL.md" | grep -q "^name: godot-refactoring"; then
    echo "  ✓ Skill name: godot-refactoring"
else
    echo "  ✗ Invalid skill name in frontmatter"
fi

if head -5 "$SKILL_DIR/SKILL.md" | grep -q "^description:"; then
    echo "  ✓ Description present"
else
    echo "  ✗ Description missing"
fi
echo ""

# Check file sizes
echo "File sizes:"
du -h "$SKILL_DIR"/*.md | sort -h
echo ""

# Total line count
total=$(wc -l "$SKILL_DIR"/*.md | tail -1 | awk '{print $1}')
echo "Total lines: $total"
echo ""

if [ "$all_present" = true ]; then
    echo "✓ Skill validation PASSED"
    echo ""
    echo "The godot-refactoring skill is ready to use!"
    exit 0
else
    echo "✗ Skill validation FAILED"
    echo ""
    echo "Some files are missing. Please check the output above."
    exit 1
fi
