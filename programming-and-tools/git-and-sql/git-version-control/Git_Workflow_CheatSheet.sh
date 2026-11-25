#!/usr/bin/env bash
# Git: Commits, Branches and Pull Requests — Quick Reference Cheatsheet

# 1. Repository Setup & Status
git init
git status
git remote add origin https://github.com/organization/ml-project.git

# 2. Staging & Committing
git add train.py src/models/
git commit -m "feat(model): add resnet backbone with focal loss"

# 3. Branching & Context Switching
git switch -c experiment/focal-loss
git branch -v
git switch main

# 4. Merging & Integration
git merge experiment/focal-loss

# 5. Inspecting History & Diff
git log --oneline --graph --decorate --all -n 10
git diff HEAD~1 HEAD
