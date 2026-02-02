# Slide 22 of Lecture 12 contains information about the Hyper-parameters.

Random search draws hyperparameters uniformly within the predefined ranges instead of exhaustively scanning a grid. For scale-sensitive values like regularization strength or learning rate, it is better to sample the logarithm uniformly; for example, rather than sampling α directly between 0.1 and 0.001, sample log(α) uniformly between −1 and −3 and then exponentiate base 10. Searching in logarithmic space helps cover several orders of magnitude more effectively.
