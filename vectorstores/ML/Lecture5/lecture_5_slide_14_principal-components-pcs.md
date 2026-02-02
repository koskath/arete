# Slide 14 of Lecture 5 contains information about the Principal Components (PCs).

The overall PC calculation process works as follows: for each PC, PCA finds a zero-centered unit vector pointing in the direction of PC. However, the direction of unit vectors returned by PCA is not stable*. If you perturb the training set slightly and run PCA again, the unit vectors may point in the opposite direction as the original vectors. Still, they will lie on the same axes, since two opposing unit vectors lie on the same axis.
