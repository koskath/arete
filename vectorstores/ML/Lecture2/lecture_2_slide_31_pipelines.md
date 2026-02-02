# Slide 31 of Lecture 2 contains information about the Pipelines.

Data transformation steps often must be executed multiple times in the correct order, so the Scikit-Learn `Pipeline` class accepts a list of (name, estimator) pairs that define the sequence, with all but the final estimator required to implement `fit_transform()`, as illustrated by `Pipeline([('imputer', SimpleImputer()), ('scaler', StandardScaler())])`.
