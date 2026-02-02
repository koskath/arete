# Slide 37 of Lecture 7 contains information about the Types of Recommender Systems.

Collaborative filtering, used by Netflix, does not assume access to side information about items and instead relies on the principle that personal tastes are correlated, so if Alice and Bob both like X and Alice likes Y, then Bob is more likely to like Y; it's a form of unsupervised learning that has a label matrix Y with ratings yij (rating of user i for movie j) but no explicit features, though it typically doesn't predict well for new users or movies that lack rating history.
