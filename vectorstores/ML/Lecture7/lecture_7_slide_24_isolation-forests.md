# Slide 24 of Lecture 7 contains information about the Isolation Forests*.

Isolation Forests are a tree-based unsupervised method that uses a collection of trees to calculate anomaly scores for each instance, with linear time complexity and good scalability; they work best with large, high-dimensional datasets and perform poorly on small datasets, use random partitioning, make no assumptions about feature distributions, and can detect anomalies without prior knowledge, though they provide no explanation for why certain instances are flagged as anomalies.
