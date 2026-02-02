# Slide 11 of Lecture 12 contains information about the Recurrent & Denoising Autoencoders.

When working with sequential data such as time series or dimensionality-reduction tasks, recurrent neural networks often make better autoencoders than dense architectures. A recurrent autoencoder typically consists of a sequence-to-vector encoder RNN that compresses the entire input sequence into a single vector, paired with a vector-to-sequence decoder RNN that reconstructs the data.

Denoising autoencoders encourage the model to learn robust features by injecting noise—either additive Gaussian noise or randomly dropped inputs—and training it to recover the original, noise-free signal. These autoencoders also serve as powerful feature extractors, as demonstrated by Pascal Vincent et al., “Extracting and Composing Robust Features with Denoising Autoencoders,” Proceedings of the 25th International Conference on Machine Learning (2008): 1096–1103.
