# Slide 30 of Lecture 13 contains information about the Adversarial Examples.

The Fast Gradient Sign Method (FGSM) efficiently generates adversarial images by passing an input through the CNN, computing the loss relative to the true label, calculating the gradient of that loss with respect to the input pixels, and then taking the sign of the gradient to craft a perturbed output.
