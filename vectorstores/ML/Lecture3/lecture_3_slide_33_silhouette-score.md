# Slide 33 of Lecture 3 contains information about the Silhouette Score.

The silhouette score helps find the optimal number of clusters by averaging the silhouette coefficient over all instances, where the coefficient is \((b-a)/\max(a,b)\) with \(a\) representing the mean distance to other points in the same cluster and \(b\) the mean distance to the nearest cluster; the value ranges from -1 to +1, and if \(k\) is too small distinct clusters merge, whereas if \(k\) is too large clusters are chopped into multiple pieces.
