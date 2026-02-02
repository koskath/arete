# Slide 22 of Lecture 7 contains information about the Local Distance-Based Outlier Detection.

The outlierness ratio for example i is calculated as the average distance of i to its k nearest neighbors divided by the average distance of those neighbors to their own k nearest neighbors, and if this outlierness ratio is greater than 1, then point x is further away from its neighbors than expected given the local density.
