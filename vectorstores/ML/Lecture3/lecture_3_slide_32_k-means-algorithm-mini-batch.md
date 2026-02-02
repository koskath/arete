# Slide 32 of Lecture 3 contains information about the K-Means Algorithm: Mini-Batch.

The mini-batch variant uses small subsets of the data at each iteration, nudging the centroids slightly and typically speeding up the algorithm by a factor of three or four, which also makes it possible to cluster massive datasets that do not fit in memory.
`from sklearn.cluster import MiniBatchKMeans`
`minibatch_kmeans = MiniBatchKMeans(n_clusters=5)`
`minibatch_kmeans.fit(X)`