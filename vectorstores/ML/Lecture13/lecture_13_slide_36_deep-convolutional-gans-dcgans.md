# Slide 36 of Lecture 13 contains information about the Deep Convolutional GANs: DCGANs.

DCGANs, introduced in 2015, adapt deeper convolutional networks to generate larger images, following several architectural guidelines: replace pooling with strided convolutions in the discriminator and transposed convolutions in the generator, apply batch normalization everywhere except the generator’s output and discriminator’s input, remove fully connected hidden layers, use ReLU activations in the generator (switching to tanh at the output), and rely on leaky ReLU throughout the discriminator. 
