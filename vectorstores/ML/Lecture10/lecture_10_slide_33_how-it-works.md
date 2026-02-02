# Slide 33 of Lecture 10 contains information about the How it works?.

Operations such as `MatMul` multiply two matrices, `Add` performs element-wise addition, and `ReLU` applies the element-wise rectified linear function defined as 0 when \(x \le 0\) and \(x\) when \(x > 0\).

Variables act as stateful nodes that output their current value, so the state—typically model parameters—is retained across multiple executions of a graph.
