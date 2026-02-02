# Slide 29 of Lecture 7 contains information about the Product Recommendation: Amazon.

Amazon's product recommendation method returns the k nearest neighbors across columns by finding j values that minimize the distance ||xi – xj||, identifying products bought by similar users, but first each column is normalized by dividing by its norm xi/||xi||, which reflects whether a product is bought by many people or just a few.
