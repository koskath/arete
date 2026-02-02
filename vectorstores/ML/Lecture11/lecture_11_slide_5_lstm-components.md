# Slide 5 of Lecture 11 contains information about the LSTM Components.

Slide 5 emphasizes that extra components inside an LSTM enable the RNN to remember and store important events from the distant past, with the input gate controlling which information is written into the long-term state or memory cell (c). Another gate regulates the flow into the input gate itself by analyzing both the current input to the LSTM cell, denoted x_t, and the previous short-term state h_{t-1} to decide what should influence the memory cell.

Notations remain as follows: previous cell state (c_{t-1}), previous hidden state (h_{t-1}), and current input x_t.
