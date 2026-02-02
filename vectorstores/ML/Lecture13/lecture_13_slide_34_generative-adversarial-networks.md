# Slide 34 of Lecture 13 contains information about the Generative Adversarial Networks.

Each GAN training iteration has two phases. First, the discriminator sees a batch composed of real images labeled 1 and an equal number of generator-produced fakes labeled 0, and it is optimized with binary cross-entropy. Second, the generator creates another batch of fake images, passes them through the discriminator (which never sees real examples in this step), and uses labels fixed at 1 so it learns to fool the critic. Many modern architectures rely on SELU (Scaled Exponential Linear Unit), a ReLU variant that automatically normalizes neuron outputs during training.

`codings_size = 30`
`generator = keras.models.Sequential([keras.layers.Dense(100, activation="selu", input_shape=[codings_size]), keras.layers.Dense(150, activation="selu"), keras.layers.Dense(1, activation="sigmoid"), keras.layers.Reshape([28, 28])])`





`discriminator = keras.models.Sequential([ keras.layers.Flatten(input_shape=[28, 28]), keras.layers.Dense(150, activation="selu"), keras.layers.Dense(100, activation="selu"), keras.layers.Dense(28 * 28, activation="sigmoid")])`
`gan = keras.models.Sequential([generator, discriminator])`


Book: Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow by Aurélien Géron
