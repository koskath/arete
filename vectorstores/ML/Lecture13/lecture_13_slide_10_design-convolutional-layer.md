# Slide 10 of Lecture 13 contains information about the Design Convolutional layer.

Designing a convolutional layer involves choosing the filter size, which represents the neuron’s receptive field as a small image-shaped weight matrix that slides across the input to perform dot products and detect edges, textures, or shapes. The stride determines how many pixels the filter steps between positions (commonly one), while padding—often zero-padding—extends the borders so that features near the edges are preserved. Larger strides shrink the feature map, speeding computation at the cost of detail.
