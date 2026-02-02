# Slide 20 of Lecture 13 contains information about the Recap: CNN.

A CNN is built from convolutional, pooling, and fully connected layers. The convolutional stage comprises filters (convolution kernels) that produce feature maps and share parameters within each map; filter size defines the receptive field, and the stride controls how many pixels the filter shifts at each step, with a stride of one being common. Pooling layers usually follow one or more convolutions to reduce feature-map dimensions before the fully connected layers aggregate the information.

During training, forward propagation flows through these layers without learning in the pooling stages, and backpropagation updates the convolutional weights based on prediction errors, a process that can demand significant RAM for deep networks.
