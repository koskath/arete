# Slide 30 of Lecture 9 contains information about the Backpropagation.

Backpropagation computes the neural network gradient via the chain rule. Computing the gradient is known as "backpropagation". With squared loss, the objective function is: \( f(v, W) = \frac{1}{2} \sum_{i=1}^{n} \left( v^{\top} h(W x_i) - y_i \right)^2 \).
The usual training procedure uses stochastic gradient descent, where we compute the gradient of a random example 'i' and update both 'v' and 'W'. The problem is highly non-convex and can be difficult to tune. For the backward pass, we must initialize all hidden layers' connection weights randomly, or else training will fail. For this algorithm to work for MLP's architecture, the step function was replaced with the logistic (sigmoid) function, σ(z) = 1 / (1 + exp(–z)).

*David Rumelhart et al. "Learning Internal Representations by Error Propagation," (Defense Technical Information Center technical report, September 1985).
