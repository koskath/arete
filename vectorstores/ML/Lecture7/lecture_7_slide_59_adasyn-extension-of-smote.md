# Slide 59 of Lecture 7 contains information about the ADASYN (extension of SMOTE).

ADASYN's sample generation technique is similar to SMOTE, but for each minority class data example xi, it generates gi = ri × g interpolated samples, where g is the total number of synthetic data samples needed and ri is proportional to the number of majority class samples among the k nearest neighbors of xi, with the highest generation rate occurring near the class boundaries.
