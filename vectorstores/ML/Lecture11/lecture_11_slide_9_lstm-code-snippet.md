# Slide 9 of Lecture 11 contains information about the LSTM Code Snippet.

This slide explains that an LSTM cell can recognize an important input, store it in the long-term state, preserve it until it becomes relevant, and then extract it exactly when needed.

## Using LSTM layer NOT SimpleRNN layer
model = keras.models.Sequential([keras.layers.LSTM(20, return_sequences=True, input_shape=[None, 1]), keras.layers.LSTM(20, return_sequences=True), keras.layers.TimeDistributed(keras.layers.Dense(10))])

## LSTMCell as an argument
model = keras.models.Sequential([keras.layers.RNN(keras.layers.LSTMCell(20), return_sequences=True, input_shape=[None, 1]), keras.layers.RNN(keras.layers.LSTMCell(20), return_sequences=True), keras.layers.TimeDistributed(keras.layers.Dense(10))])

The snippet highlights using LSTMCell as an argument and favoring the LSTM layer rather than a SimpleRNN layer, reinforcing the guidance presented on slide 9 and attributed to “Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow” by Aurélien Géron.


