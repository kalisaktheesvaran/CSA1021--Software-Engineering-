#!/usr/bin/env bash
set -e
W=$(mktemp -d); cd "$W"; git init -q -b main demo; cd demo
git config user.email s@example.com; git config user.name Student
printf 'def greet():\n    return "Hello"\n' > app.py; git add .; git commit -qm "Initial app.py"
echo "### Create two branches that edit the SAME line"
git checkout -q -b feature-a; sed -i 's/"Hello"/"Hello, World"/' app.py; git commit -qam "feature-a: change greeting"
git checkout -q main; git checkout -q -b feature-b; sed -i 's/"Hello"/"Hi there"/' app.py; git commit -qam "feature-b: change greeting"
git checkout -q main
echo "### git branch"; git branch
echo "### Merge feature-a (fast-forward, no conflict)"; git merge feature-a
echo "### Merge feature-b -> CONFLICT"; git merge feature-b || true
echo "### git status"; git status --short
echo "### Conflicted file"; cat app.py
echo "### Resolve: keep a combined version"
printf 'def greet():\n    return "Hello, World - Hi there"\n' > app.py
git add app.py; git commit -qm "Resolve merge conflict between feature-a and feature-b"
echo "### Final history"; git log --oneline --graph --all
git branch -d feature-a feature-b
