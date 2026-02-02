# Slide 14 of Lecture 9 contains information about the Activation Function.

The activation function defines how the weighted sum of input is transformed to output from a node or nodes. All hidden layers use the same activation function, while the output layer uses a different activation function from the hidden layers. Large DNNs with nonlinear activations can theoretically approximate any continuous function. The Sigmoid (S-shaped) activation function was good, but ReLU works better in ANNs. Softmax ensures all estimated probabilities are between 0 and 1 and they add up to 1, which is required for exclusive classes.
16
Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow by Aurélien Géron, 2019.
