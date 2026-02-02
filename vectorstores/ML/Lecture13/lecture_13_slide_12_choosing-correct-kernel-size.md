# Slide 12 of Lecture 13 contains information about the Choosing "Correct" Kernel Size.

Kernel size controls the receptive field of each convolution and must match the data’s characteristics: small kernels capture fine-grained, local patterns and suit smaller inputs, while larger kernels detect broader structures in bigger images but demand more resources. Stacking several layers of small kernels can approximate a wider context without losing detail, whereas excessively large kernels risk over-smoothing and erasing subtle features.
