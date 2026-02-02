# Slide 25 of Lecture 10 contains information about the Distributed ML: Parallelization.

Model parallelism splits the deep-learning model itself so that each worker loads a different portion for training, beginning with the workers that own the input layer and receive the training data directly.

During the forward pass, each segment computes its output signal and hands it to the workers hosting the next layer, while during backpropagation the gradients start at the workers holding the output layer and propagate back toward the workers that manage the input layers, as described by Mayer, Ruben, and Hans-Arno Jacobsen in “Scalable deep learning on distributed infrastructures: Challenges, techniques, and tools,” ACM Computing Surveys (CSUR) 53.1 (2020): 1–37.
