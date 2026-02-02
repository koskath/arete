# Slide 26 of Lecture 12 contains information about the Hyper-parameter Optimization Frameworks.

Several frameworks support hyper-parameter optimization out of the box. In scikit-learn, `GridSearchCV` implements grid search while `RandomizedSearchCV` performs random search over user-defined distributions. On the TensorFlow side, Trieste (https://github.com/secondmind-labs/trieste) provides a Bayesian optimization toolbox that integrates tightly with TensorFlow workflows. 
