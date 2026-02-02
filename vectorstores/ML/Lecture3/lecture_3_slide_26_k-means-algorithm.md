# Slide 26 of Lecture 3 contains information about the K-Means Algorithm.

If centroids are given, every instance in the dataset can be labeled by assigning it to the cluster with the nearest centroid; if labels are given, centroids are easily located by averaging the instances within each cluster. When neither labels nor centroids are available, K-Means begins with random centroid placement for k instances, alternates between labeling instances and updating centroids, and repeats until the centroids stop moving, guaranteeing convergence in a finite number of steps.
