# Slide 36 of Lecture 5 contains information about the Decision Tree Training Algorithm.

Given a set of labeled training instances, the decision tree training algorithm recursively builds the tree by first checking whether all instances in the current subset share the same class (in which case it creates a leaf with that label), otherwise picking the best attribute test to split the data, partitioning the training set according to the test outcomes, and then repeating this process on each subset until stopping conditions are met.
