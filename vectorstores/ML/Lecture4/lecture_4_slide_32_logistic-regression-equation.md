# Slide 32 of Lecture 4 contains information about the Logistic Regression Equation.

`Logit(pi) = 1/(1 + exp(-pi))`
`ln(pi/(1-pi)) = Beta_0 + Beta_1*X_1 + ... + B_k*K_k`

In the logistic regression equation, logit(pi) is the dependent variable and x is the independent variable, with beta parameters estimated via maximum likelihood estimation (MLE) by iteratively testing different values of beta to optimize the log odds fit, maximizing the log-likelihood function to obtain the best parameter estimates, and then using the resulting coefficients to compute conditional probabilities for each observation, which are logged and summed to yield predicted probabilities; in binary classification, probabilities below 0.5 are typically mapped to class 0 and those above to class 1, and model quality is assessed by how well it predicts the dependent variable (goodness of fit).
