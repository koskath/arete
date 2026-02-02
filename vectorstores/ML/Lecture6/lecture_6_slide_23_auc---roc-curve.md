# Slide 23 of Lecture 6 contains information about the AUC - ROC Curve.

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
`# below are the probabilities obtained from a hypothetical model that doesn't always predict the mode`
`y_proba_2 = np.array(np.random.uniform(0, .7, n_0).tolist() + np.random.uniform(.3, 1, n_1).tolist())`
`y_pred_2 = y_proba_2 > .5`
`import matplotlib.pyplot as plt`
`def plot_roc_curve(true_y, y_prob):`
`    """`
`    plots the roc curve based of the probabilities`
`    """`
`    fpr, tpr, thresholds = roc_curve(true_y, y_prob)`
`    plt.plot(fpr, tpr)`
`    plt.xlabel('False Positive Rate')`
`    plt.ylabel('True Positive Rate') `