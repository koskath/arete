# Slide 6 of Lecture 11 contains information about the LSTM Components.

Slide 6 elaborates on the forget gate, which regulates how much information in the long-term state persists across time instants, and it reiterates that the components of LSTM cells are implemented as fully connected neural networks. It also points out related recurrent variants with memory cells—peephole connections and gated recurrent units—before describing the output gate that determines how much information leaves the cell at each time instant and thereby controls the values of h_t (short-term state) and y_t (output at time t).

Notations continue to follow earlier slides: previous cell state (c_{t-1}), previous hidden state (h_{t-1}), and current input x_t.
