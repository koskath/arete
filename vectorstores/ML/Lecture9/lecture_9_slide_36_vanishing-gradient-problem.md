# Slide 36 (Bonus Slide) of Lecture 9 contains information about the Vanishing Gradient Problem.

Vanishing gradients make it difficult to know which direction the parameters should move to improve the cost function. Exploding gradients can make learning unstable. Away from the origin, the gradient is nearly zero. The problem gets worse when you take the sigmoid of a sigmoid, and in deep networks, many gradients can be nearly zero everywhere.
39
