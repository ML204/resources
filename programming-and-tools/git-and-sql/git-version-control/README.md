# Git: Commits, Branches and Pull Requests

Study notes, reference cheatsheets, and command recipes for **Git Version Control for Machine Learning**.

---

## 📌 Overview & Mental Model

Git is a content-addressed, distributed version control system that models project history as a cryptographic **Directed Acyclic Graph (DAG)** of immutable commit snapshots.

```
Working Directory  ──(git add)──>  Staging Area (Index)  ──(git commit)──>  Local Repo (.git)  ──(git push)──>  Remote (GitHub)
```

### The Three-Way Reproducibility Triangle in ML
1. **Code**: Tracked via Git commit SHA hashes.
2. **Data**: Tracked via Git LFS, DVC, or cloud bucket hashes.
3. **Environment**: Tracked via lockfiles (`uv.lock`, `poetry.lock`) and Docker container digests.

---

## 🛠️ Essential Git CLI Commands for ML

### 1. Staging & Committing
```bash
# Check modified files and branch state
git status

# Stage specific files (avoid indiscriminate git add .)
git add train.py src/models/transformer.py

# Commit with Conventional Commits format
git commit -m "feat(model): implement rotary positional embeddings (RoPE)"
```

### 2. Branching & Context Switching
```bash
# Create and switch to an experimental branch
git switch -c experiment/focal-loss

# List branches with latest commit info
git branch -v

# Return to main
git switch main

# Fast-forward or 3-way merge
git merge experiment/focal-loss
```

### 3. Inspecting Diffs & History
```bash
# Compare unstaged working directory against staging area
git diff

# Compare staged changes against HEAD
git diff --staged

# View compact visual commit graph
git log --oneline --graph --decorate --all -n 15
```

### 4. Git LFS (Large File Storage)
```bash
# Install Git LFS extension
git lfs install

# Track large model checkpoints and binary datasets
git lfs track "*.pt"
git lfs track "*.safetensors"
git lfs track "*.parquet"

# Commit tracking rules
git add .gitattributes
git commit -m "chore(lfs): track binary model checkpoints"
```

---

## 📁 Repository Files
- `Git_Workflow_CheatSheet.sh`: Ready-to-run shell script summarizing real-world Git operations and conflict resolution workflows.
