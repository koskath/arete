# Slide 8 of Lecture 10 contains information about the Recurrent Neural Networks (RNNs).

RNNs were developed to solve learning problems such as time-series or other sequential tasks where information about past instants or events is directly linked to making future predictions, which is why the recurrent neuron maintains a memory, or state, from past computations.

Data is looped back into the same neuron at every new time instant so that the neuron takes the previous output \(y_{t-1}\) alongside the current input \(x_t\), and to support this loop the recurrent neuron uses two input weights, \(W_{x_t}\) and \(W_{y_{t-1}}\), a relationship highlighted throughout Slide 8.
