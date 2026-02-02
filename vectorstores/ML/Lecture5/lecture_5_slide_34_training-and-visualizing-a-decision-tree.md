# Slide 34 of Lecture 5 contains information about the Training and Visualizing a Decision Tree.

To train and visualize a decision tree for classifying iris flowers, you can load the iris dataset, train a shallow tree (for example with `DecisionTreeClassifier(max_depth=2)`) on petal length and width, and then export the tree with `export_graphviz` to inspect splits such as “Is petal length greater than 2.45 cm?” and “Is petal width smaller than 1.75 cm?”, taking advantage of the fact that decision trees require very little data preparation and no feature scaling.

from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz
iris= load_iris()
X= iris.data[:, 2:] #petal length and width 
y = iris.target than 2.45 cm
tree_clf =DecisionTreeClassifier(max_depth=2) 
tree_clf.fit(X, y) 
export_graphviz( tree_clf, out_file=image_path("iris_tree.dot"), feature_names=iris.feature_names[2:], class_names=iris.target_names, rounded=True, filled=True)

