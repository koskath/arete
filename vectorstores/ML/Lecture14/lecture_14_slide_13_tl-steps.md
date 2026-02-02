# Slide 13 of Lecture 14 contains information about the TL Steps.

Transfer learning generally follows three steps. First, select a pre-trained model whose prior knowledge relates to the new task. Second, configure it by freezing some of the original layers to preserve the learned representations, removing the final layer, and adding new layers whose weights start randomly and will adapt to the target task. Third, train the augmented network on the target domain data. 
