# Slide 40 of Lecture 9 contains information about the Leaky ReLU.

Some gradients can still die out during backpropagation with a large learning rate, which is why we use Leaky ReLU. Leaky ReLU works by setting the activation to a small negative slope when the value x < 0.
43
Bisong E. (2019) More on Optimization Techniques. In: Building Machine Learning and Deep Learning Models on Google Cloud Platform. Apress, Berkeley, CA
