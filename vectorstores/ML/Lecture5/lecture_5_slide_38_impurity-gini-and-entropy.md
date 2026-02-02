# Slide 38 of Lecture 5 contains information about the Impurity: Gini and entropy.

The Gini index is an impurity measure used to split decision trees by estimating the probability that a randomly chosen instance would be misclassified if it were labeled according to the class distribution in a node; it works with categorical targets, returns values between 0 (perfect purity) and 0.5 for binary classification, and helps identify which attribute provides the most information about the class, so a Gini impurity greater than 0.5 at the root suggests the node is roughly evenly split among classes (for example, with class counts [50, 50, 50]), making classification harder without further splitting.

Formula: \[ G_i = 1 - \sum_{k=1}^{n} p_{i,k}^2 \]
