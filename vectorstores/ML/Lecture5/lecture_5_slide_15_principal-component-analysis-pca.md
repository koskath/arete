# Slide 15 of Lecture 5 contains information about the Principal Component Analysis (PCA).

To decide how many principal components to retain, we look at the proportion of variance explained (PVE), which measures what percentage of the total variance is captured by a given set of PCs and can be approximated for the m-th PC as the m-th eigenvalue divided by the number of PCs; for an n*p (observations * variables) data matrix X, there can be up to min(n - 1, p) PCs, but there is no single fixed rule for selecting how many to use.


Here is a code snippet in PCA:

` # Access the first principal component (PC1)`
`pc1 = pca.components_[0]`

`# Get feature names and their corresponding contributions to PC1`
`feature_contributions = pd.DataFrame(pc1, index=X.columns, columns=["PC1"])`
`print("Features contributing to the first principal component (PC1):")`
`print(feature_contributions)`

`# Sort the features by the absolute value of their contributions to PC1`
`sorted_features = feature_contributions.abs().sort_values(by="PC1", ascending=False)`

`# Get the names of the features that contribute to the first principal component`
`top_features = sorted_features.index.tolist()`

`# Print out the feature names sorted by contribution`
`print("Features contributing to the first principal component (PC1):")`
`print(top_features)`


**Output:**
Features contributing to the first principal component (PC1):
                PC1
Month          0.002627
Year           0.000108
Patient_Visits 0.999997
Features contributing to the first principal component (PC1):
['Patient_Visits', 'Month', 'Year'] ` 