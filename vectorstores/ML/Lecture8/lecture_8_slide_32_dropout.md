# Slide 32 of Lecture 8 contains information about the Dropout.

In this example, we apply dropout only to neurons in the top one-to-three layers, excluding the output layer. Suppose p = 50%: during testing, a neuron would be connected to twice as many input neurons as it would be on average during training. To compensate for this fact, a rule of thumb is to multiply each input connection weight by the keep probability (1 – p) after training. Alternatively, we can divide each neuron's output by the keep probability during training.
