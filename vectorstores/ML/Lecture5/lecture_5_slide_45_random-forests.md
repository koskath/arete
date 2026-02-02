# Slide 45 of Lecture 5 contains information about the Random Forests.

• RandomForestClassifier has all hyperparameters of a DecisionTreeClassifier (mostly).
• Can control growth of trees.
• Hyperparameters of a BaggingClassifier to control the ensemble.
• Random Forest algorithm introduces extra randomness when growing trees
• Searches for best feature among a random subset of features.
• Results in greater tree diversity --> overall better model.
bag_clf = BaggingClassifier(DecisionTreeClassifier(splitter="random", max_leaf_nodes=16), n_estimators=500, max_samples=1.0, bootstrap=True, n_jobs=-1)

Each tree is trained using 100% of the available training data. 
Eahc tree is trained on a randomly sampled subset

