# Structuring ML Project Repositories

Reference architecture, templates, and best practices for **Structuring Machine Learning Project Repositories**.

---

## 🏗️ The Cookiecutter Data Science Pattern

```
ml-project/
├── data/                            # Medallion data architecture
│   ├── raw/                         # Bronze tier: Immutable original data (read-only!)
│   ├── interim/                     # Silver tier: Cleansed, transformed tables
│   └── processed/                   # Gold tier: Final feature matrices & tensors
├── notebooks/                       # Exploratory analysis (numbered sequentially)
│   ├── 01_eda.ipynb
│   └── 02_baseline_model.ipynb
├── src/                             # Reusable production package
│   ├── __init__.py
│   ├── data/make_dataset.py
│   ├── features/build_features.py
│   ├── models/train.py
│   └── utils/helpers.py
├── configs/                         # Type-safe YAML configurations
│   └── config.yaml
├── models/                          # Serialized weights (local / Git LFS)
├── tests/                           # Automated unit tests (pytest)
├── Dockerfile                       # Multi-stage production container
├── .gitignore                       # Explicit exclusion rules
├── requirements.txt                 # Dependencies
└── README.md                        # Documentation
```

---

## 🛡️ Critical Golden Rules

1. **`data/raw/` is Strictly Read-Only**: Never edit raw data files in place. All cleaning logic must be reproducible code that outputs into `data/interim/` or `data/processed/`.
2. **Never Hardcode File Paths**: Use Python's `pathlib.Path` relative to the project root to guarantee OS portability across macOS, Linux, and Windows.
3. **Strict `.gitignore` Exclusion**: Never commit raw datasets, credentials (`.env`), virtual environments (`.venv`), or heavy checkpoint weights (`*.pt`) directly to Git.
4. **Prefer Modern Model Serialization**: Use Hugging Face `SafeTensors` (`.safetensors`) or `ONNX` (`.onnx`) rather than vulnerable Python `pickle` objects.

---

## 📁 Repository Files
- `ML_Project_Structure_Template.py`: Python utility script that programmatically scaffolds the entire directory tree and default `.gitignore`.
