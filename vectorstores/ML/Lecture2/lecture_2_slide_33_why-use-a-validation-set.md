# Slide 33 of Lecture 2 contains information about the Why use a validation set?.

Fine-tuning an ML model is an iterative process aimed at improving performance on both the training data and unseen examples, so to ensure generalization it is best to evaluate on a validation set during hyperparameter tuning rather than touching the test set. The test set, also called the holdout set, should be reserved for the final model to obtain an unbiased evaluation and to confirm that overfitting has not occurred.
