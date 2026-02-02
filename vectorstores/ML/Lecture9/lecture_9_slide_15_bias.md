# Slide 15 of Lecture 9 contains information about the Bias.

Generalization error consists of three different errors: Bias, Variance, and Irreducible error due to the noisiness of data. Bias happens due to wrong assumptions. A high-bias model is most likely to underfit the training data. An example would be assuming data is linear when it is actually quadratic. Note that if you train a linear SVM model using the LinearSVC class from Sci-kit, the LinearSVC class regularizes the bias term.
17
