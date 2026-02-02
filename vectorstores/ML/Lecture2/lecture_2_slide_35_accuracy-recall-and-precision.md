# Slide 35 of Lecture 2 contains information about the Accuracy, Recall and Precision.

Accuracy is the proportion of all classifications that were correct, whether positive or negative, and it serves as a rough indicator of training progress or convergence for balanced datasets, while recall (true positive rate) measures the proportion of actual positives correctly identified and precision captures the share of the model's positive predictions that are truly positive. Here, TP denotes true positives, FN false negatives, and FP false positives. Do not use recall and precision in extremely imbalanced datasets where the number of actual positives is very, very low.

* Accuracy = Correct Classification / Total Classifications = TP + TN / TP + TN + FP + FN * 
* Recall (or TPR) = correctly classified actual positives / all actual positives = TP / TP + FN *
* Precision = correctly classified actual positives / everything classified a spositive = TP / TP + FP * 

