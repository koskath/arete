# Slide 26 of Lecture 6 contains information about the Regression Metrics.

Mean Absolute Error (MAE) is the average absolute difference between ground-truth and predicted values, is robust to outliers, but does not indicate whether errors are due to under- or over-prediction and is technically non-differentiable, while Mean Squared Error (MSE) averages the squared differences between targets and predictions, is easier to optimize but more sensitive to outliers because squaring amplifies even small errors, potentially leading to overestimation; in code, MAE and MSE can be computed with `mae = np.abs(y - y_hat)` and `mse = (y - y_hat)**2` and summarized with their means and standard deviations.

MSE Formula: \[ MSE = \frac{1}{N} \sum_{j=1}^{N} (y_j - \tilde{y}_j)^2 \]
MAE Formula: \[ MAE = \frac{1}{n} \sum_{i=1}^{n} |y_i - \hat{y}_i| \]


