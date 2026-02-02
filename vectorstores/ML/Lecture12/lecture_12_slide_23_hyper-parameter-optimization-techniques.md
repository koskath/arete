# Slide 23 of Lecture 12 contains information about the Hyper-parameter Optimization Techniques.

The “babysitting,” “trial and error,” or “grad student descent” approach relies entirely on manual tuning and is still widely practiced despite the growing complexity of models. As the number of hyperparameters increases, evaluations become time-consuming and interactions become highly non-linear, making manual iteration inefficient.

Grid search remains one of the most commonly used techniques; it is an exhaustive, brute-force evaluation of the Cartesian product of user-specified hyperparameter values. Unfortunately, the method scales poorly because the number of evaluations grows exponentially with each additional hyperparameter. 
