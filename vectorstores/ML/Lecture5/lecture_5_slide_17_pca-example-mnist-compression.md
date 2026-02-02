# Slide 17 of Lecture 5 contains information about the PCA Example: MNIST Compression.

In the MNIST compression example, PCA is applied to preserve 95% of the dataset’s variance, reducing each instance from 784 features to just over 150 while shrinking the overall dataset to less than 20% of its original size.

Here is a code snippet:
`pca = PCA(n_components = 154)`
`X_reduced = pca.fit_transform(X_train)`
`X_recovered = pca.inverse_transform(X_reduced)`


# Here is what is depicted in The image in slide 17 of lecture 5:
The image compares the original and compressed versions of handwritten digits from the MNIST dataset, a common benchmark in machine learning for image processing. On the left, you see the "Original" images, and on the right, the "Compressed" images.

This compression likely involves a technique such as Principal Component Analysis (PCA), which reduces dimensionality while preserving variance. In this case, 95% of the variance is maintained. This process is crucial in deep learning and machine learning because it reduces data size and complexity, allowing for faster processing and more efficient storage without significantly compromising information quality. Such compressed data can still train models effectively, making MNIST a practical example of impactful data handling techniques.
