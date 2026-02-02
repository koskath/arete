# Slide 20 of Lecture 10 contains information about the Model Training.

Model training generally follows three steps: build a computational graph from the network definition, feed in training data to compute the loss function, and update the parameters accordingly.

Define-and-run frameworks such as TensorFlow and Caffe complete the graph construction phase before the data phase, whereas define-by-run frameworks like PyTorch combine the first two steps so that the computational graph is built dynamically during training instead of being predetermined.

This distinction is explored further at https://www.oreilly.com/content/complex-neural-networks-made-easy-by-chainer/.
