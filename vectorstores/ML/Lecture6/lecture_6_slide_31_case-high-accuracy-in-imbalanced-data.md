# Slide 31 of Lecture 6 contains information about the Case: High Accuracy in Imbalanced Data.

`import numpy as np`
`from sklearn.metrics import accuracy_score, confusion_matrix, roc_auc_score, roc_curve`
`n = 10000`
`ratio = .95`
`n_0 = int((1-ratio) * n)`
`n_1 = int(ratio * n)`
`y = np.array([0] * n_0 + [1] * n_1)`
`# below are the probabilities obtained from a hypothetical model that always predicts the majority class`
`# probability of predicting class 1 is going to be 100%`
`y_proba = np.array([1]*n)`
`y_pred = y_proba > .5`
`print(f'accuracy score: {accuracy_score(y, y_pred)}')`
`print('Confusion matrix')`
`cf_mat = confusion_matrix(y, y_pred)`
`print(cf_mat)`
`print(f'class 0 accuracy: {cf_mat[0][0]/n_0}')`
`print(f'class 1 accuracy: {cf_mat[1][1]/n_1}')`

Imbalance: Majority of values are one
