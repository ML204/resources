# Ordinary Least Squares (OLS) — Quick Reference Summary

## Core Concept
Ordinary Least Squares (OLS) is the closed-form algebraic and statistical method for estimating the parameters of a linear regression model by minimizing the sum of squared differences (residuals) between observed and predicted values.

## Objective Function
$$\mathcal{L}(\theta) = \sum_{i=1}^m \left( y^{(i)} - \hat{y}^{(i)} \right)^2 = \|y - X\theta\|_2^2$$

## Closed-Form Solution (The Normal Equation)
Taking the matrix derivative with respect to $\theta$ and setting it to zero:
$$\nabla_\theta \|y - X\theta\|_2^2 = -2X^T (y - X\theta) = 0$$
$$X^T X \theta = X^T y$$
$$\theta^* = (X^T X)^{-1} X^T y$$

where:
- $X \in \mathbb{R}^{m \times (n+1)}$ is the design matrix with a leading column of ones for the bias/intercept.
- $y \in \mathbb{R}^m$ is the target vector.
- $(X^T X)^{-1} X^T$ is known as the **Moore-Penrose Pseudoinverse** $X^\dagger$.

## Key Geometric Intuition
The predicted vector $\hat{y} = X\theta^*$ is the **orthogonal projection** of the actual target vector $y$ onto the column space $\text{col}(X)$. The residual vector $e = y - \hat{y}$ is strictly orthogonal to every feature column in $X$.

## Assumptions of Classical OLS (Gauss-Markov Theorem)
1. **Linearity**: The relationship between $X$ and $y$ is linear in parameters.
2. **Full Rank (No Multicollinearity)**: $X^T X$ must be invertible (features are linearly independent).
3. **Exogeneity**: $\mathbb{E}[\varepsilon | X] = 0$ (residuals have zero conditional expectation).
4. **Homoscedasticity**: $\text{Var}(\varepsilon | X) = \sigma^2 I$ (constant error variance).
5. **No Autocorrelation**: Residuals are uncorrelated with each other.

Under these conditions, OLS is the **BLUE** (Best Linear Unbiased Estimator).

## Computational Complexity
- Matrix inversion of $X^T X$: $\mathcal{O}(n^3)$ or $\mathcal{O}(n^{2.81})$.
- Optimal when $n$ (features) is modest ($n < 10,000$). For very large $n$ or streaming data, iterative **Gradient Descent** is preferred.
