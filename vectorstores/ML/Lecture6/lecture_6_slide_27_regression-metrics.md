# Slide 27 of Lecture 6 contains information about the Regression Metrics.

Root Mean Squared Error (RMSE) is the square root of the average squared difference between target and predicted values—essentially the square root of MSE—which brings the error back to the original units of the target and tends to be less sensitive to small errors than raw MSE while still penalizing larger deviations; in practice, it can be computed via `mse = (y - y_hat)**2`, `rmse = np.sqrt(mse.mean())`, and then reported as `print(f"RMSE: {rmse:0.2f}")`.

RMSE Formula: [\ RMSE = \sqrt{\frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2} \]