# Slide 20 of Lecture 12 contains information about the Learning Rate Scheduling.

Learning-rate schedules gradually reduce the step size during training to maintain stability while continuing to make progress. Power scheduling sets the learning rate as a function of the iteration number, η(t) = η₀ / (1 + t / s)ᶜ, where the initial rate η₀, the power c (often 1), and the step scale s are hyperparameters. Exponential scheduling uses η(t) = η₀ · 0.1^(t/s), causing the rate to drop by a factor of 10 every s steps.

Piecewise-constant scheduling keeps the rate fixed for a block of epochs, for example η₀ = 0.1 for five epochs followed by η₁ = 0.001 for the next fifty, and continues with additional plateaus as needed. Performance scheduling ties the adjustment to validation metrics by measuring the error every N steps and reducing the learning rate by a factor λ whenever the error stops improving.
