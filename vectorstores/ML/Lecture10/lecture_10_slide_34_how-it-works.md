# Slide 34 of Lecture 10 contains information about the How it works?.

Placeholders are nodes whose value—such as inputs or labels—is supplied at execution time, and the following code illustrates how TensorFlow uses variables and placeholders to define a computation graph:
import tensorflow as tf
b = tf.Variable(tf.zeros((100,)))
W = tf.Variable(tf.random_uniform((784, 100), -1, 1))
x = tf.placeholder(tf.float32, (1, 784))
h = tf.nn.relu(tf.matmul(x, W) + b)

Once defined, the graph can be deployed with a session on either CPU or GPU hardware depending on availability and performance needs.
35
