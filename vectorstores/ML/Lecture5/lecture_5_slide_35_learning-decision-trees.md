# Slide 35 of Lecture 5 contains information about the Learning Decision Trees.

Given a set of training examples, learning a decision tree means constructing the questions you can ask and searching for the “best” tree to describe the data, but since there are far too many possible trees even with a small number of features, it is computationally infeasible to enumerate them all, so trees are built greedily by repeatedly choosing important questions for each node that best split the data and thereby determine the internal structure of the tree.
