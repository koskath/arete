# Slide 4 of Lecture 10 contains information about the BatchNorm.

The vanishing gradients problem can be alleviated with better weight initialization, stronger optimizers, or Batch Normalization, which has emerged as one of the most successful architectural innovations in deep learning because it stabilizes the minibatch distribution of inputs to each network layer during training [1][2].

BatchNorm works by letting the model learn the optimal scale and mean of every layer’s inputs: an operation inserted just before or after the activation function zero-centers and normalizes each hidden-layer input, and a subsequent scaling and shifting step applies learned vectors per layer to fine-tune the normalized values.

1. Sergey Ioffe and Christian Szegedy, “Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift,” Proceedings of the 32nd International Conference on Machine Learning (2015): 448–456.
2. Santurkar, Shibani, et al. "How does batch normalization help optimization?." Advances in Neural Information Processing Systems. 2018.
