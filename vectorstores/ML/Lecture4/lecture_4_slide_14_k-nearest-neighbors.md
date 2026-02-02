# Slide 14 of Lecture 4 contains information about the K-nearest neighbors.

Given a training dataset X and a new instance (x_{\text{new}}\), KNN finds the k points in \(X\) closest to \(x_{\text{new}}\) using the chosen distance metric, then predicts a label for \(x_{\text{new}}\) either by taking a majority vote among the k nearest neighbors for classification or by averaging their values for regression, as implemented for example in `sklearn.neighbors.KNeighborsClassifier`.
