# Vectors and Matrices — Quick Reference Summary

## Key Formulas
- **Vector Norm (L2)**: $\|v\|_2 = \sqrt{v_1^2 + v_2^2 + \dots + v_n^2}$
- **Dot Product**: $u \cdot v = \sum_{i=1}^n u_i v_i = \|u\| \|v\| \cos \theta$
- **Matrix Shape**: $X \in \mathbb{R}^{m \times n}$ where $m$ is samples, $n$ is features.

## Useful Python / NumPy Snippets
```python
import numpy as np

# Vector definition
v = np.array([3.0, 2.0])
u = np.array([1.0, 3.0])

# Magnitude
norm_v = np.linalg.norm(v)

# Vector addition
sum_vu = v + u

# Scalar multiplication
scaled = 2.5 * v
```
