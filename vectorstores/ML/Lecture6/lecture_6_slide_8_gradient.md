# Slide 8 of Lecture 6 contains information about the Gradient.

In gradient boosting, the ensemble initially consists of a single tree whose predictions match that first tree’s outputs, then a second tree is trained on the residual errors of the first so that the ensemble’s predictions become the sum of the two trees’ outputs, and a third tree is trained on the residuals of the second, with the ensemble’s predictions improving as more trees are added.
