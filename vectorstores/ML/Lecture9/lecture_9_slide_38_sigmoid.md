# Slide 38 (Bonus Slide) of Lecture 9 contains information about the Sigmoid.

Consider setting 'h' to define binary features z. Each h(z ) can be viewed as a binary feature. We can make 2k objects by all the possible "part combinations". However, this is hard to optimize because it is non-differentiable or discontinuous. The Sigmoid is a smooth approximation to these binary features.

\( 
h(z_{ic}) = 
\begin{cases}
1 & \text{if } z_{ic} \ge 0 \\
0 & \text{if } z_{ic} < 0
\end{cases}
\)

