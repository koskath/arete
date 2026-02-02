# Slide 33 of Lecture 8 contains information about the Dropout.

Make sure to evaluate training loss after training. If the model overfits the training set, increase the dropout rate. If the model underfits the training set, decrease the dropout rate. Dropout can be applied to hidden neurons, either between two hidden layers or between the last hidden layer and the output layer. The dropout rate works as a weight constraint on selected layers. There is a time-effort trade-off: well-tuned dropout significantly slows down convergence but results in a much better model.
