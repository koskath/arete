# Slide 30 of Lecture 3 contains information about the K-Means Algorithm.

The algorithm is guaranteed to converge but may settle on a local optimum rather than the global best solution, and this outcome depends heavily on how the centroids are initialized.

```python
kmeans = KMeans(n_clusters=5, init=good_init, n_init=1)
```

n_init is hyperparameter
The algorithm will run 10 times