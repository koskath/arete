# Slide 16 of Lecture 6 contains information about the SVM: Kernel.

SVMs naturally classify linearly separable data, such as in text classification, but when the data are not linearly separable you can use a kernel function—which is not part of SVM itself but provides dot products in an implicit feature space—so that SVM only needs dot products rather than explicit vectors, avoiding expensive computations; with a linear kernel the classifier remains linear, while nonlinear kernels yield nonlinear decision boundaries without explicitly transforming the data.
