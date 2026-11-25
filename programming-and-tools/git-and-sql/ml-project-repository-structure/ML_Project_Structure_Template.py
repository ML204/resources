#!/usr/bin/env python3
"""
ML Project Repository Structure Generator
Scaffolds an industry-standard (Cookiecutter Data Science) project layout.
"""

from pathlib import Path

DIRECTORIES = [
    "data/raw",
    "data/interim",
    "data/processed",
    "notebooks",
    "src/data",
    "src/features",
    "src/models",
    "src/visualization",
    "configs",
    "models",
    "tests",
]

GITIGNORE_CONTENT = """# Python & Virtualenv
__pycache__/
*.py[cod]
.venv/
venv/
.env

# Data & Checkpoints
data/raw/*
data/interim/*
data/processed/*
!data/raw/.gitkeep
models/*.pt
models/*.onnx

# Jupyter
.ipynb_checkpoints/
.pytest_cache/
"""

def scaffold():
    base = Path.cwd()
    for dir_path in DIRECTORIES:
        p = base / dir_path
        p.mkdir(parents=True, exist_ok=True)
        # Add .gitkeep to ensure empty directories are retained
        gitkeep = p / ".gitkeep"
        if not gitkeep.exists():
            gitkeep.touch()

    gitignore = base / ".gitignore"
    if not gitignore.exists():
        gitignore.write_text(GITIGNORE_CONTENT)

    print("✅ ML Project Repository layout successfully generated!")

if __name__ == "__main__":
    scaffold()
