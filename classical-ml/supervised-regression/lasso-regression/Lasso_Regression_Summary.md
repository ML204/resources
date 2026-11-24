# Lasso Regression (L1 Regularization) — Quick Reference Summary

## Core Concept
Lasso (Least Absolute Shrinkage and Selection Operator) penalizes the absolute value of coefficients (L1 norm). Because the diamond-shaped L1 constraint ball has sharp corners on the coordinate axes, the optimization contours naturally touch the axes first, driving non-essential coefficients to **exactly zero**. This produces **sparse models** and performs automatic feature selection.

## Objective Function
$$\mathcal{L}_{\text{Lasso}}(\theta) = \frac{1}{2m} \|y - X\theta\|_2^2 + \lambda \|\theta\|_1 = \frac{1}{2m} \sum_{i=1}^m (y^{(i)} - \hat{y}^{(i)})^2 + \lambda \sum_{j=1}^n |\theta_j|$$

where:
- $\lambda \ge 0$ controls the sparsity penalty strength.
- Larger $\lambda$ forces more feature coefficients to exactly zero.

## Optimization: Coordinate Descent & Soft-Thresholding
The L1 norm $|\theta_j|$ is non-differentiable at $\theta_j = 0$, so no closed-form matrix solution exists. Instead, it is solved using **Coordinate Descent** via the **Soft-Thresholding Operator** $S_{\lambda}$:

$$S_{\lambda}(z) = \text{sign}(z) \cdot \max(0, |z| - \lambda)$$

$$\theta_j^{(k+1)} = \frac{S_{\lambda}\left(\sum_{i=1}^m x_{ij} (y^{(i)} - \sum_{k \ne j} x_{ik} \theta_k)\right)}{\sum_{i=1}^m x_{ij}^2}$$

## Key Properties: Ridge vs. Lasso
| Property | Ridge Regression (L2) | Lasso Regression (L1) |
| :--- | :--- | :--- |
| **Penalty Term** | $\lambda \sum \theta_j^2$ | $\lambda \sum \|\theta_j\|$ |
| **Solution Form** | Closed-form: $(X^TX + \lambda I)^{-1} X^Ty$ | Iterative (Coordinate Descent) |
| **Sparsity** | Coefficients approach zero, never reach 0 | Sets irrelevant coefficients to **exactly 0** |
| **Feature Selection** | No (retains all features) | **Yes** (inherent variable selection) |
| **Correlated Features** | Shrinks coefficients equally | Arbitrarily picks one and sets others to 0 |
| **Bayesian Prior** | Gaussian prior $\mathcal{N}(0, \sigma^2)$ | Laplace prior $\text{Laplace}(0, b)$ |
