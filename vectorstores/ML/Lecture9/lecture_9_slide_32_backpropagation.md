# Slide 32 of Lecture 9 contains information about the Backpropagation.

(Computing gradients) Backpropagation is an efficient technique for computing gradients automatically. The Backpropagation training algorithm is used to train MLPs. For each training instance, the backpropagation algorithm first makes a prediction in a forward pass and measures the error. Then it goes through each layer in reverse to measure the error contribution from each connection in a backward pass. Finally, it tweaks the connection weights to reduce error in a Gradient Descent step.
35
*David Rumelhart et al. "Learning Internal Representations by Error Propagation," (Defense Technical Information Center technical report, September
1985).
