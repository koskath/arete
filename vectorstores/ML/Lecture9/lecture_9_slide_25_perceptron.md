# Slide 25 of Lecture 9 contains information about the Perceptron.

How is a Perceptron trained? The Perceptron training algorithm was largely inspired by Hebb's rule, also known as Hebbian learning. The process works as follows: first, the Perceptron is fed one training instance at a time, and for each instance it makes its predictions. Second, for every output neuron that produced a wrong prediction, it reinforces the connection weights from the inputs that would have contributed to the correct prediction. The Heaviside step function is used in Perceptrons, and common step functions used in Perceptrons assume a threshold of 0. The signum function extracts the sign of a real number z. The Perceptron and SGDClassifier both have similar implementations.
27
