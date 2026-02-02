# Here is what the image 1 in slide 14 of lecture 8 contains:


The images collectively describe and contrast two fundamental optimization algorithms in machine learning: **Gradient Descent (GD)** and **Stochastic Gradient (SG)**.

Gradient Descent (GD) Principle and Visualization

The GD image focuses on finding a **local minimum** of a cost function $f(w)$, where $w$ are the model parameters. The method's core principle is that the **direction of the largest decrease** in the function's value is the negative gradient, $-\nabla f(w)$. The accompanying visualization shows the iterative process of moving along a cost curve:
* If the slope (gradient) $\nabla f(w^t)$ is **negative**, the algorithm moves to a **more positive** $w$ (right) to decrease the function value.
* If the slope is **positive**, the algorithm moves in the **negative direction** (left).
A critical practical tip provided for GD is to **ensure all features have a similar scale**, which helps the optimization path converge more directly and efficiently. 



Stochastic Gradient (SG) Algorithm

The SG image describes the **Stochastic Gradient (SG)** algorithm, an iterative optimization algorithm primarily used to **minimize averages** (like the average loss over a dataset). The key difference from standard GD lies in the gradient calculation:
* The algorithm starts with an **initial guess, $w^0$**.
* In the update step, $w^{t+1} = w^t - \alpha \nabla f_i(w^t)$, the gradient is calculated **for a random training example '$i$'** instead of the entire dataset.
* This process is **repeated successively** using a new random example in each step.
The image highlights the computational efficiency of SG: the **Gradient Cost: Gradient is independent of 'n'** (the total number of training examples). Consequently, the **Iterations are 'n' times faster than GD iterations**, making SG the preferred choice for training models on very large datasets. 