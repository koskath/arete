# Slide 34 of Lecture 2 contains information about the Cross-validation.

Cross-validation provides a less biased, less optimistic estimate of model performance than a simple train/test split, typically via K-fold cross validation where k denotes the number of splits, as in `KFold(n_splits=10, random_state=42, shuffle=False)`.
