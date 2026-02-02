# Slide 19 of Lecture 8 contains information about the Batch and Mini-Batch GD.

At each Gradient Descent step, it calculates the whole batch of training data. This is slow on very large training sets, but it scales well with the number of features. Mini-batch GD computes gradients on small random sets of instances called mini-batches. It is faster than Stochastic GD. Batch GD stops at the minimum, which is slow. SGD and Mini-batch GD continue to walk around, which is faster. All algorithms output similar models and predict in exactly the same way.
