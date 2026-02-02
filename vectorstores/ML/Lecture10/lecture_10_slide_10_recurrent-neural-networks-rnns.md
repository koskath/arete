# Slide 10 of Lecture 10 contains information about the Recurrent Neural Networks (RNNs).

Computations within a recurrent layer hinge on each neuron receiving both the output of the previous layer and its current input, supported by two weight vectors that differentiate between the temporal and feedforward contributions.

Each neuron performs an affine transformation of these combined inputs, passes the result through a nonlinear activation function such as tanh, and the recurrent layer’s outputs are then sent to a dense or fully connected layer whose softmax activation produces the desired class probabilities.
