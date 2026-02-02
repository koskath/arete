# Slide 18 of Lecture 12 contains information about the Learning Rate: Setting the Step-Size.

Stochastic gradient descent is highly sensitive to the choice of step size, especially in deep models. A common strategy is to run SGD for a period with a fixed learning rate, periodically measure and plot the error, and reduce the step size if progress stalls. Bias terms sometimes benefit from a dedicated multiplier that allows a larger effective step, and many practitioners add momentum—moving βₜ, often around 0.9, in the previous update direction—to stabilize and accelerate convergence.
