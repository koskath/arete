# Slide 18 of Lecture 6 contains information about the SVM and IRIS Data set.

`# import data`
`iris = datasets.load_iris()`
`# Take the first two features.`
`X = iris.data[:, :2]`
`y = iris.target`
`# SVM`
`C = 1.0 # SVM regularization parameter`
`models = ( svm.SVC(kernel="linear", C=C), svm.LinearSVC(C=C, max_iter=10000), svm.SVC(kernel="rbf", gamma=0.7, C=C), svm.SVC(kernel="poly", degree=3, gamma="auto", C=C),)`

Helpful link: https://scikit-learn.org/stable/modules/svm.html
