# Slide 43 of Lecture 3 contains information about the DBSCAN Algorithm.

DBSCAN defines clusters as continuous regions of high density by counting how many instances lie within each point’s epsilon neighborhood; if an instance has at least `min_samples` neighbors it becomes a core point, all instances within a core point’s neighborhood join the same cluster (possibly chaining through other core points), and any instance that is neither a core point nor adjacent to one is labeled an anomaly, so the algorithm works best when all clusters are sufficiently dense.
