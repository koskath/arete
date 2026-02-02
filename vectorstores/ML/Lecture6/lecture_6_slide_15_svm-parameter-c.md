# Slide 15 of Lecture 6 contains information about the SVM: Parameter C.

C in SVM controls the trade-off between training error and the flatness of the decision boundary by determining how strongly outliers are penalized: a larger C typically reduces training error but can hurt generalization, while a smaller C yields a flatter, more regularized classifier; grid search is often used to tune C, and in RBF-SVM there are two key parameters to select—C and gamma, which governs the radius of the radial basis function.
