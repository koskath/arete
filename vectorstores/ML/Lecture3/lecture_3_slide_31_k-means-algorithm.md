# Slide 31 of Lecture 3 contains information about the K-Means Algorithm.

Centroid initialization can be controlled by setting the `init` hyperparameter to a NumPy array of centroid positions, setting `n_init` to 1 when you already know roughly where the centroids should be, or by running the algorithm multiple times with different random starts and keeping the best solution; `n_init` is the hyperparameter that governs this behavior and defaults to 10, meaning the algorithm runs ten times and selects the best outcome.
