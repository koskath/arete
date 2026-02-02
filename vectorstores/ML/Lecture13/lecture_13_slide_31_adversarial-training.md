# Slide 31 of Lecture 13 contains information about the Adversarial Training.

Adversarial training teaches models to classify manipulated inputs correctly by optimizing the usual loss to reduce prediction errors while anticipating attackers who use the same loss to maximize errors. The attacker typically computes the gradient with respect to the input, takes its sign, scales it by a threshold, and adds the result to create adversarial versions alongside the normal and noisy samples illustrated from top to bottom.
