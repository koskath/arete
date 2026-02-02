# Slide 10 of Lecture 12 contains information about the Convolution Autoencoder.

To build an autoencoder for images, the architecture generally becomes a convolutional autoencoder. The encoder behaves like a conventional CNN composed of convolution and pooling layers that reduce spatial dimensions (height and width) while expanding depth via additional feature maps. The decoder then reverses this process by upscaling the image and reducing its depth back to the original dimensions, typically using transpose convolutional layers.
