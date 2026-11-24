# Ridge Regression (L2 Regularization) — Quick Reference Summary

## Core Concept
Ridge Regression (also known as Tikhonov regularization) adds a squared L2 norm penalty on weight coefficients to the standard OLS loss function. This shrinks coefficients toward zero, stabilizes estimates in the presence of multicollinearity, and prevents overfitting by reducing model variance.

## Objective Function
$$\mathcal{L}_{\text{Ridge}}(\theta) = \|y - X\theta\|_2^2 + \lambda \|\theta\|_2^2 = \sum_{i=1}^m (y^{(i)} - \hat{y}^{(i)})^2 + \lambda \sum_{j=1}^n \theta_j^2$$

where:
- $\lambda \ge 0$ is the regularization hyperparameter (complexity penalty).
- Note: The intercept $\theta_0$ is generally **not** penalized.
- Features should always be **standardized** (zero mean, unit variance) before applying Ridge.

## Closed-Form Solution
$$\nabla_\theta \mathcal{L}_{\text{Ridge}} = -2X^T (y - X\theta) + 2\lambda \theta = 0$$
$$(X^T X + \lambda I) \theta = X^T y$$
$$\theta_{\text{Ridge}}^* = (X^T X + \lambda I)^{-1} X^T y$$

### Why $X^T X + \lambda I$ is always invertible:
Even if $X^T X$ is singular (non-invertible due to collinearity or when features $n >$ samples $m$), adding $\lambda I$ shifts all eigenvalues upward by $\lambda > 0$, guaranteeing positive-definiteness and invertibility.

## Key Properties
- **Shrinkage, Not Sparsity**: Coefficients are shrunk toward zero but never reach exactly zero (unless $\lambda \to \infty$). Thus, Ridge retains all features.
- **Bias-Variance Tradeoff**: As $\lambda$ increases, bias increases and variance decreases.
- **Bayesian Interpretation**: Ridge Regression is equivalent to Maximum A Posteriori (MAP) linear estimation with a **Gaussian prior** on the weights $\theta \sim \mathcal{N}(0, \sigma^2 I)$.
