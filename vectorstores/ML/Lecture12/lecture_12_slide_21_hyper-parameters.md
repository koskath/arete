# Slide 21 of Lecture 12 contains information about the Hyper-parameters.

One way to select candidate hyperparameters is grid search, where every combination of chosen values is evaluated to identify the best configuration. However, the number of grid points grows exponentially with the number of hyperparameters: testing five parameters with ten values each already requires 10⁵ = 100,000 training runs. Because of this explosive cost, grid-based exploration is rarely the best option.
