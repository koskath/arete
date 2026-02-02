# Slide 14 of Lecture 10 contains information about the Recurrent Network Training.

RNNs are trained with backpropagation through time because standard backpropagation cannot directly handle the looped or recurrent structure, yet the overall idea remains the same: calculate the error gradient, move backward from the output layer through the hidden layers, and adjust the network weights accordingly.

In a recurrent neuron we effectively have a single neural cell with connections to itself, so we conceptually unroll the cell across time steps, each time step \(t\) being called a frame, and this perspective also clarifies how a deep RNN stacks multiple layers of such cells.
