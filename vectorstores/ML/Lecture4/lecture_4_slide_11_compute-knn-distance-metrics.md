# Slide 11 of Lecture 4 contains information about the Compute KNN: Distance Metrics.

The goal when computing KNN is to identify the nearest neighbors of a given query point so that we can assign an appropriate class label, which requires choosing a distance metric—most commonly Euclidean or Manhattan distance—that measures absolute differences between points and is defined for real-valued vectors.

**Euclidean distance:** Popular distance measure. It is limited to real valued vectors
Formula: \[d(x, y) = \sqrt{\sum_{i=1}^{n} (x_i - y_i)^2}\]

**Manhattan distance:**  Measures absolute value between two points 
Formula: \[d(x, y) = \sum_{i=1}^{n} |x_i - y_i|\]

**Minkowski distance:**  Generalized form of Euclidean and Manhattan distance metrics.
Formula: \[d(x, y) = \left( \sum_{i=1}^{n} |x_i - y_i|^p \right)^{1/p}\]
