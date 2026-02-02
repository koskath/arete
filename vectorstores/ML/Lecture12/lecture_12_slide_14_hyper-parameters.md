# Slide 14 of Lecture 12 contains information about the Hyper-parameters.

Neural networks expose numerous hyperparameters, such as the learning rate or the strength of regularization, that regulate the overall model design. These hyperparameters differ from the fundamental parameters—the connection weights—which are optimized via backpropagation after the hyperparameters have been selected manually or through a tuning phase.

To avoid overfitting, hyperparameters should not be tuned on the same data used for stochastic gradient descent. Instead, a dedicated validation split is held out, and model performance is evaluated across various hyperparameter configurations on this set to ensure the training data is not memorized. 
