# Slide 12 of Lecture 12 contains information about the Recap.

Autoencoders learn to copy their inputs to their outputs by compressing the data into an efficient latent representation and reconstructing something close to the original. They consist of an encoder, or recognition network, that maps inputs into the latent space and a decoder, or generative network, that transforms the internal representation back to the output domain.

The cost function includes a reconstruction loss that penalizes differences between inputs and outputs. Architecturally, an autoencoder mirrors a multilayer perceptron, with the added constraint that the number of output neurons equals the number of inputs so the network can reproduce the original signal.

Recurrent autoencoders apply the same idea to sequences: a sequence-to-vector RNN encoder compresses the entire sequence into a single vector, and a vector-to-sequence RNN decoder recreates the temporal structure. Across these variants, autoencoders remain powerful tools for dimensionality reduction and visualization.
