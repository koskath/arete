# Slide 37 of Lecture 13 contains information about the Recap: GANs.

GANs train generative models by mapping random noise vectors to outputs that mimic a target data distribution such as images. The framework revolves around a generator that transforms Gaussian noise into realistic samples and a discriminator that receives either genuine training images or generator outputs and predicts authenticity.

Each iteration alternates discriminator training—feeding mixed batches of real (label 1) and fake (label 0) data—with generator training, in which newly produced fake images are labeled 1 so the generator learns to fool the discriminator. Because both networks continuously adapt, the competition may stagnate before reaching a stable equilibrium if neither side gains a decisive advantage.
