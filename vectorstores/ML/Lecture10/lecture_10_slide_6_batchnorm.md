# Slide 6 of Lecture 10 contains information about the BatchNorm.

Batch Normalization is tricky to use in RNNs even though it is sufficient for other network types, so Gradient Clipping is often applied in RNNs to mitigate the exploding gradients problem by limiting gradient magnitudes during backpropagation, yet that same clipping technique does not help with vanishing gradients.

BN acts like a regularizer that reduces the need for other techniques such as dropout, but it also adds a runtime penalty to the neural network and makes each epoch slower whenever BN remains in use, as discussed by Pascanu, Razvan, Tomas Mikolov, and Yoshua Bengio in “On the difficulty of training recurrent neural networks,” International Conference on Machine Learning, 2013.
