# Slide 7 of Lecture 6 contains information about the Gradient Boosting.

The basic steps of gradient boosting are to fit an additive ensemble model in a forward stage-wise manner, introducing a weak learner at each stage to compensate for the shortcomings of the existing learners, with those shortcomings identified by the gradients that indicate how to improve the model; in practice, this can be implemented with `sklearn.ensemble.GradientBoostingClassifier(n_estimators=100, learning_rate=1.0, max_depth=1, random_state=0).fit(X_train, y_train)`, where `max_depth` limits the depth of individual regression trees and `n_estimators` controls the number of boosting stages.
from sklearn.ensemble import GradientBoostingClassifier
GradientBoostingClassifier(n_estimators=100, learning_rate=1.0, ... max_depth=1,
random_state=0).fit(X_train, y_train)
Maximum depth of the individual regression
estimators. (limits the no of nodes in tree)
No of boosting stages to
perform.
