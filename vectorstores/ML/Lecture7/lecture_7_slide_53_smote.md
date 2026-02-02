# Slide 53 of Lecture 7 contains information about the SMOTE.

The SMOTE algorithm works by finding k-nearest neighbors for each sample, randomly selecting samples from those k-nearest neighbors (depending on the required oversampling amount), computing new samples as the original samples plus the difference multiplied by a random gap between 0 and 1, adding these new samples to the minority class, and finally creating a new balanced dataset.
