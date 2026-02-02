# Slide 31 of Lecture 8 contains information about the Dropout*.

Dropout is a popular regularization technique for deep neural networks. Neural networks get a 1–2% accuracy boost simply by adding dropout. How it works: at every training step, every input neuron has a probability (p) of being temporarily "dropped out." This means it will be entirely ignored during this training step, but it may be active during the next step. After training, neurons don't get dropped anymore. The hyperparameter p is called the dropout rate, which is set between 10% and 50%. For example, RNNs use dropout rates closer to 20-30%, while CNNs use dropout rates closer to 40-50%.

