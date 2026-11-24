# Gradient Descent — Quick Reference Summary

## Key Formulas
- **Update Rule**: $\theta_{t+1} = \theta_t - \eta \nabla J(\theta_t)$
- **Learning Rate**: $\eta > 0$ controls step size along the negative gradient direction.
- **Mean Squared Error Gradient**: $\nabla_\theta J(\theta) = \frac{1}{m} X^T (X\theta - y)$

## Variants
- **Batch Gradient Descent (BGD)**: Computes the exact gradient using the entire dataset ($m$ samples) per step. Stable convergence, slow for massive data.
- **Stochastic Gradient Descent (SGD)**: Updates parameters using a single random sample per iteration. Fast, noisy trajectories, escapes local minima.
- **Mini-Batch Gradient Descent (MBGD)**: Computes gradients over batches of size $B \in [32, 256]$. Standard practice in modern machine learning.

## Python / NumPy Implementation
```python
import numpy as np

def gradient_descent(X, y, lr=0.01, epochs=1000):
    m, n = X.shape
    theta = np.zeros(n)
    for _ in range(epochs):
        gradient = (1 / m) * X.T @ (X @ theta - y)
        theta -= lr * gradient
    return theta
```
