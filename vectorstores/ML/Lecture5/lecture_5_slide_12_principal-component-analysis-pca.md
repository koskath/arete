# Slide 12 of Lecture 5 contains information about the Principal Component Analysis (PCA).


PCA is influenced by magnitude of each variable. The first PC (PC1) of a data set is a linear combination of features that has the largest variance. The second PC (PC2) is a linear combination of data sets that has maximal variance out of all linear combinations that are uncorrelated with PC1. Furthermore, PCs are uncorrelated with each other, and PCs form a basis of new space (true for irrespective of dimensions).
Here is a helpful link: https://uc-r.github.io/pca

Here is a code snippet:
`from sklearn.decomposition import PCA`
`pca = PCA(n_components = 2)`
