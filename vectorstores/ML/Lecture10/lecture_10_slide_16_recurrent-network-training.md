# Slide 16 of Lecture 10 contains information about the Recurrent Network Training.

The main challenge in training RNNs is the vanishing and exploding gradient problem that arises because long-term dependencies across many unrolled time instants make gradients either decay away or blow up.

Gradient clipping, BatchNorm, and ReLU activations can mitigate these issues, yet the combination of exploding and vanishing gradients and the tendency to discard information from early time instances ultimately motivated the creation of the Long Short-Term Memory (LSTM) memory cell.
