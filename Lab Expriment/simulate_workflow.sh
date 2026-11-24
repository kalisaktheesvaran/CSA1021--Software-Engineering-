#!/usr/bin/env bash
# Local simulation of the fork -> clone -> branch -> push -> pull-request -> merge workflow.
# "upstream" and "fork" are bare repos standing in for GitHub repositories.
set -e
W=$(mktemp -d); cd "$W"
git config --global user.email "student@example.com" >/dev/null 2>&1 || true
git config --global user.name "Student" >/dev/null 2>&1 || true
git config --global init.defaultBranch main
echo "### 1. Owner creates upstream repo"
git init -q --bare upstream.git
git clone -q upstream.git owner && cd owner
echo "# Demo Project" > README.md; git add .; git commit -qm "Initial commit"; git push -q origin main; cd ..
echo "### 2. Contributor FORKS (copy of upstream)"
git clone -q --bare upstream.git fork.git
echo "### 3. Contributor clones the fork & adds upstream remote"
git clone -q fork.git contributor && cd contributor
git remote add upstream ../upstream.git; git remote -v
echo "### 4. Create feature branch, commit, push to fork"
git checkout -q -b feature/add-greeting
echo "print('Hello from contributor')" > greet.py; git add .; git commit -qm "Add greeting script"
git push -q origin feature/add-greeting; git branch -a; cd ..
echo "### 5. PULL REQUEST: owner reviews and merges the contributor's branch (what GitHub's Merge button does)"
cd owner
git remote add contributor ../fork.git; git fetch -q contributor
git log --oneline main..contributor/feature/add-greeting
git merge --no-ff -q contributor/feature/add-greeting -m "Merge pull request #1 from contributor/feature/add-greeting"
git push -q origin main; cd ..
echo "### 6. Contributor syncs fork with upstream"
cd contributor; git checkout -q main; git pull -q upstream main; git log --oneline --graph
