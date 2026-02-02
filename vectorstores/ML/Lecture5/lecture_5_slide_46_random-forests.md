# Slide 46 of Lecture 5 contains information about the Random Forests.

• Tree growth in a Random Forest: at each node only a random
subset of features is considered for splitting.
• Possible to make trees more random by using random thresholds for each feature.
• Easy to measure relative importance of each feature (weighted average).
• Ex: Trains a RandomForestClassifier on the iris dataset and outputs each feature’s importance.
from sklearn.datasets import load_iris iris = load_iris()

rnd_clf = RandomForestClassifier(n_estimators=500, n_jobs=-1)
rnd_clf.fit(iris["data"], iris["target"])
for name, score in zip(iris["feature_names"], rnd_clf.feature_importances_):
    print(name, score)

sepal length (cm) 0.112492250999
sepal width (cm) 0.0231192882825
petal length (cm) 0.441030464364
petal width (cm) 0.423357996355

Most important features are petal length (44%) and petal width (42%)