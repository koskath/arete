# Slide 16 of Lecture 4 contains information about the Compute KNN: Code.
`from sklearn.neighbors import KNeighborsClassifier`
`model_name = ‘K-Nearest Neighbor Classifier’`
`knnClassifier = KNeighborsClassifier(n_neighbors = 5, metric = ‘minkowski’, p=2)`
`knn_model = Pipeline(steps=[(‘preprocessor’, preprocessorForFeatures), (‘classifier’, knnClassifier)])`
`knn_model.fit(X_train, y_train)`
`y_pred = knn_model.predict(X_test)`