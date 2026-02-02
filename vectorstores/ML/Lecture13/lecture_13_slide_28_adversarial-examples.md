# Slide 28 of Lecture 13 contains information about the Adversarial Examples.

Deep-learning systems face both white-box attacks, where adversaries know the training data, initialization, algorithm, and hyperparameters, and black-box attacks, where that knowledge is limited; in either case, carefully crafted small perturbations can yield poor performance. Traditional regularizers like weight decay or dropout are insufficient, so robustness often relies on brute-force adversarial training in which the model is exposed to generated adversarial examples during learning.
