# Slide 29 of Lecture 10 contains information about the What is TensorFlow?.

TensorFlow’s core is very similar to NumPy but adds GPU support, and the key idea is to express every numeric computation as a graph in which nodes are operations with any number of inputs and outputs while edges are tensors that flow between those nodes.

These computation graphs can be exported to portable formats so that models can be trained in one environment and run in another, and TensorFlow’s core features include tf.keras, data loading and preprocessing utilities (tf.data, tf.io), image processing (tf.image), and signal processing (tf.signal).
