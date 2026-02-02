# Slide 27 of Lecture 13 contains information about the Adversarial Examples.

In the adversarial setting, a model that normally performs tasks such as classification now faces an attacker who tries to induce errors, so the objective becomes maintaining comparable accuracy even under attack. Image-based attacks come in untargeted forms, where the adversary merely pushes the model toward any wrong label, and targeted forms, where the adversary forces a specific incorrect label.

# Here is what the image 1 in slide 27 of lecture 13 contains:

On the left side of the image is a picture of a panda bear with an abstracted background primarily consisting of dark and light hues. Below this image, the letter "x" is present. Underneath the symbol "x," text reads \( y = \text{"panda"} \) with a confidence of "57.7%."

To the right of the panda image, there is a mathematical expression "+ .007 ×". This leads to another image located in the center of the arrangement, showing random colorful static noise with a wide distribution of colors such as red, green, blue, and yellow. Below this image, the expression \(\text{sign}(\nabla_x J(\theta, x, y))\) is shown. Underneath this formula, text states "nematode" with a confidence level of "8.2%."

Further to the right, the expression "=" is displayed. Next to this is an image that mirrors the initial image of the panda, indicating it is visually similar, if not identical. Below this image, the expression \( x + \epsilon \, \text{sign}(\nabla_x J(\theta, x, y))\) is present. The text beneath reads "gibbon" with a confidence level of "99.3%."

The composition of the image illustrates a transition starting from an original input ("panda"), adds a calculated perturbation, and results in a modified interpretation ("gibbon").