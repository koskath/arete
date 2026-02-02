# Slide 28 of Lecture 10 contains information about the What is TensorFlow?.

TensorFlow (tf) offers tools, libraries, and an open-source platform for ML, combining the Python-based Keras high-level API with low-level primitives for numerical computation using data-flow graphs.

It was developed by the Google Brain Team to support ML research, and it now provides both Python and C++ APIs for production-ready deployments.

To install, run:
$ pip install tensorflow
$ pip install tensorflow-cpu (CPU-only package)

Sample code:
import tensorflow as tf
tf.add(1, 2).numpy()
