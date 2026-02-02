# Slide 35 of Lecture 3 contains information about the Elbow Method.

The elbow method seeks the optimal (k) value by locating the point where the graph forms an elbow: you iterate over a hyperparameter-defined range of (k) values, compute the within-cluster sum of squares (WCSS) for each, and observe how well points cluster around their centroids, though many practitioners prefer the silhouette score because it is more effective when the elbow point is unclear and the elbow method can yield ambiguous results.
