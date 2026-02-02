# Slide 44 of Lecture 5 contains information about the Random Forests.


• Random Forest is an ensemble of Decision Trees.
• Trained via bagging method.
• Random Forest Classifier more convenient and optimized for Decision Trees.
• Random Forest classifier with 500 trees:

(Lower number of leaf nodes restricts the depth of each tree -> reducing overfitting)

from sklearn.ensemble import RandomForestClassifier
rnd_clf = RandomForestClassifier(n_estimators=500, max_leaf_nodes=16, n_jobs=-1)
rnd_clf.fit(X_train, y_train)
y_pred_rf = rnd_clf.predict(X_test)
