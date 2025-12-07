#!/bin/bash
#
# Setup script to install git hooks
#

echo "🔧 Setting up git hooks for Advent of Code 2025..."
echo ""

# Check if .git directory exists
if [ ! -d ".git" ]; then
    echo "❌ Error: Not a git repository"
    echo "Run 'git init' first"
    exit 1
fi

# Create hooks directory if it doesn't exist
mkdir -p .git/hooks

# Install pre-push hook
cat > .git/hooks/pre-push << 'EOF'
#!/bin/sh
#
# Pre-push hook to run regression tests
# This prevents pushing code that breaks existing solutions

echo "🧪 Running regression tests before push..."
echo ""

# Run the test suite
python3 test_solutions.py

# Capture exit code
TEST_EXIT_CODE=$?

if [ $TEST_EXIT_CODE -ne 0 ]; then
    echo ""
    echo "❌ Tests failed! Push aborted."
    echo "Fix the failing tests before pushing."
    echo ""
    echo "To bypass this check (not recommended):"
    echo "  git push --no-verify"
    echo ""
    exit 1
fi

echo ""
echo "✅ All tests passed! Proceeding with push..."
echo ""

exit 0
EOF

# Make hook executable
chmod +x .git/hooks/pre-push

echo "✅ Pre-push hook installed!"
echo ""
echo "The hook will:"
echo "  • Run regression tests before every push"
echo "  • Prevent pushing broken code"
echo "  • Ensure all solutions remain correct"
echo ""
echo "To bypass the hook (not recommended):"
echo "  git push --no-verify"
echo ""

exit 0

