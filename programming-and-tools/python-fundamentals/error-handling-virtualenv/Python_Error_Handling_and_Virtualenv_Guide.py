"""
Python Error Handling & Virtual Environments Reference Guide
=============================================================
Author: MLTheta Team (Md. Inzamamul Lohani)
Topic: Error Handling, Custom Exceptions, Defensive ML Pipelines, and Virtualenv Architecture
License: MIT

This script provides production-grade recipes and beginner-friendly walk-throughs
for error handling, resource management, and reproducible environment setups.
"""

import sys
import os
import contextlib
from typing import Any, List, Optional


# =====================================================================
# 1. THE COMPLETE TRY / EXCEPT / ELSE / FINALLY PATTERN
# =====================================================================
def load_and_preprocess_dataset(filepath: str) -> Optional[List[float]]:
    """Demonstrates complete error handling lifecycle with all four blocks:
    - try: Code that might fail
    - except: Specific exception recovery
    - else: Executes ONLY when try completes WITHOUT errors
    - finally: Always executes for deterministic cleanup
    """
    file_handle = None
    print(f"\n--- Loading Dataset from: '{filepath}' ---")
    try:
        # Check existence before opening
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"Dataset path does not exist on disk: {filepath}")

        file_handle = open(filepath, "r", encoding="utf-8")
        raw_lines = file_handle.readlines()
        data = [float(line.strip()) for line in raw_lines if line.strip()]

    except FileNotFoundError as fnf_err:
        print(f"❌ Handled FileNotFoundError: {fnf_err}")
        return None
    except ValueError as val_err:
        print(f"❌ Data Corruption Error: Could not convert entry to float ({val_err})")
        return None
    except Exception as generic_err:
        print(f"⚠️ Unexpected system error occurred: {generic_err}")
        raise
    else:
        print(f"✅ Successfully loaded {len(data)} valid numerical records.")
        return data
    finally:
        if file_handle and not file_handle.closed:
            file_handle.close()
            print("🔒 Deterministic cleanup: File handle safely closed.")


# =====================================================================
# 2. CUSTOM EXCEPTION HIERARCHY FOR MACHINE LEARNING
# =====================================================================
class MLEngineeringError(Exception):
    """Base exception for all ML pipeline and data validation errors."""
    pass


class DataValidationError(MLEngineeringError):
    """Raised when an incoming batch has invalid shapes, NaNs, or schema drift."""
    def __init__(self, message: str, sample_index: Optional[int] = None):
        super().__init__(message)
        self.sample_index = sample_index


class ModelConvergenceError(MLEngineeringError):
    """Raised when an optimization algorithm diverges or hits NaN loss."""
    def __init__(self, epoch: int, loss: float):
        super().__init__(f"Model training diverged at epoch {epoch} with loss: {loss}")
        self.epoch = epoch
        self.loss = loss


def train_step_mock(features: List[float], epoch: int):
    """Demonstrates raising domain-specific exceptions."""
    if any(x < 0 for x in features):
        raise DataValidationError("Feature values must be strictly non-negative", sample_index=0)
    
    # Simulate numeric explosion
    loss = float('inf') if epoch > 5 else 0.05
    if loss != loss or loss > 1e6 or loss == float('inf'):  # NaN or Inf check
        raise ModelConvergenceError(epoch=epoch, loss=loss)


# =====================================================================
# 3. DEFENSIVE CONTEXT MANAGERS WITH CONTEXTLIB
# =====================================================================
@contextlib.contextmanager
def execution_timer(task_name: str):
    """A clean, reusable context manager to benchmark training blocks."""
    import time
    start = time.perf_counter()
    print(f"\n⏱️ Starting task: [{task_name}]")
    try:
        yield
    finally:
        elapsed = time.perf_counter() - start
        print(f"⏱️ Finished task: [{task_name}] in {elapsed:.4f} seconds.")


# =====================================================================
# 4. VIRTUAL ENVIRONMENT CLI RECIPES & REPRODUCIBILITY
# =====================================================================
VIRTUALENV_CLI_GUIDE = """
=====================================================================
📦 Virtual Environments: Terminal Command Cheat Sheet
=====================================================================

1. Create an isolated virtual environment:
   $ python3 -m venv .venv

2. Activate the environment:
   # macOS / Linux (bash/zsh):
   $ source .venv/bin/activate
   # Windows (PowerShell):
   > .venv\\Scripts\\Activate.ps1
   # Windows (Command Prompt):
   > .venv\\Scripts\\activate.bat

3. Upgrade pip and install pinned dependencies:
   $ pip install --upgrade pip
   $ pip install numpy pandas scikit-learn matplotlib

4. Export an exact lockfile for reproducibility:
   $ pip freeze > requirements.txt

5. Replicate the exact environment on another machine:
   $ python3 -m venv .venv
   $ source .venv/bin/activate
   $ pip install -r requirements.txt

6. Deactivate and return to system Python:
   $ deactivate
=====================================================================
"""


# =====================================================================
# DEMO EXECUTION
# =====================================================================
if __name__ == "__main__":
    print("=" * 60)
    print("MLTheta Python Error Handling & Virtual Environments Demo")
    print("=" * 60)

    # 1. Test complete try-except-else-finally
    load_and_preprocess_dataset("non_existent_features.csv")

    # 2. Test custom domain exceptions
    try:
        print("\n--- Testing Custom ML Exceptions ---")
        train_step_mock([1.2, -0.5, 3.4], epoch=1)
    except DataValidationError as dve:
        print(f"Caught custom validation error: {dve} (Sample: {dve.sample_index})")

    try:
        train_step_mock([1.0, 2.0, 3.0], epoch=10)
    except ModelConvergenceError as mce:
        print(f"Caught convergence error: {mce} (Epoch: {mce.epoch}, Loss: {mce.loss})")

    # 3. Test context manager
    with execution_timer("Simulated Neural Layer Forward Pass"):
        total = sum(i ** 2 for i in range(100_000))

    # 4. Display Virtualenv Guide
    print(VIRTUALENV_CLI_GUIDE)
    print("✅ All error handling and virtual environment checks passed successfully.")
