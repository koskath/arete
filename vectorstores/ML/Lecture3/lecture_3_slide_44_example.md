# Slide 44 of Lecture 3 contains information about the Example.

`from sklearn.cluster import DBSCAN`
`from sklearn.datasets import make_moons` <-- moons dataset
`X, y = make_moons(n_samples=1000, noise=0.05)`
`dbscan = DBSCAN(eps=0.05, min_samples=5)`
`dbscan.fit(X)`


Using the moons dataset, widening each instance’s neighborhood by increasing epsilon to 0.2 produces a better clustering that reveals seven different clusters and highlights anomalies.
