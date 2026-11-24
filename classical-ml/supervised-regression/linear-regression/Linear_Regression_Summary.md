# Linear Regression — Quick Reference Summary

## Core Concept
Linear regression models the relationship between a continuous scalar dependent variable $y$ and one or more explanatory independent variables $X$ using a linear predictor function.

## Hypothesis Representation
$$\hat{y} = h_\theta(x) = \theta_0 + \theta_1 x_1 + \theta_2 x_2 + \dots + \theta_n x_n = \theta^T x$$

where:
- $x = [1, x_1, x_2, \dots, x_n]^T$ is the feature vector with bias term $x_0 = 1$.
- $\theta = [\theta_0, \theta_1, \dots, \theta_n]^T$ is the parameter/weight vector.

## Loss Function: Mean Squared Error (MSE)
$$J(\theta) = \frac{1}{2m} \sum_{i=1}^m \left( h_\theta(x^{(i)}) - y^{(i)} \right)^2$$

## Solving Methods
1. **Ordinary Least Squares (Closed Form)**:
   $$\theta^* = (X^T X)^{-1} X^T y$$
2. **Gradient Descent (Iterative)**:
   $$\theta_j := \theta_j - \alpha \frac{1}{m} \sum_{i=1}^m \left( h_\theta(x^{(i)}) - y^{(i)} \right) x_j^{(i)}$$

## Evaluation Metrics
- **Mean Squared Error (MSE)**: $\frac{1}{m} \sum (y_i - \hat{y}_i)^2$
- **Root Mean Squared Error (RMSE)**: $\sqrt{\text{MSE}}$
- **Mean Absolute Error (MAE)**: $\frac{1}{m} \sum |y_i - \hat{y}_i|$
- **Coefficient of Determination ($R^2$)**: $1 - \frac{\sum (y_i - \hat{y}_i)^2}{\sum (y_i - \bar{y})^2}$
