# Slide 5 of Lecture 10 contains information about the BatchNorm.

If you add a BN layer as the very first layer of your neural network, you no longer need to standardize your training set manually because the BN layer takes over that responsibility, and by doing so it reduces the vanishing gradients problem enough that activation functions can continue tackling the remaining difficulty.

Batch Normalization can therefore improve many deep neural networks, a point emphasized by Bisong E. (2019) in *More on Optimization Techniques*, within *Building Machine Learning and Deep Learning Models on Google Cloud Platform*, Apress, Berkeley, CA.
