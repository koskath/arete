# Slide 10 of Lecture 9 contains information about the Linearity and Non-Linearity.

We start with a linear latent-factor model with linear regression. We use features from the latent-factor model: z =Wx. Then we make predictions using a linear model: y =vTz. For non-linearity, we transform z by a non-linear function 'h': z=Wx ==> y=vTh(z). The function 'h' transforms 'k' inputs to 'k' outputs. A common choice for 'h' is the Sigmoid function. For training, we apply SGD: compute the gradient of a random example 'i', and update both 'v' and 'W'.
12
CPSC 340: Machine Learning and Data Mining: http://www.stat.yale.edu/Courses/ 1997-98/101/stat101.htm
