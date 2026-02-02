# Slide 39 of Lecture 5 contains information about the Impurity: Gini and Entropy.

Entropy measures disorder and serves as another impurity metric: a set has zero entropy when it contains instances of only one class, and the reduction in entropy achieved by a split—called information gain—is computed as the parent node’s entropy minus the weighted sum of its child nodes’ entropies, with entropy ranging from 0 (perfectly pure) up to log_2(n) for n classes at maximum impurity.

Formula:
$$H_i = -\sum_{k=1}^{n} p_{i,k} \log_2(p_{i,k})$$
where $p_{i,k} \neq 0$