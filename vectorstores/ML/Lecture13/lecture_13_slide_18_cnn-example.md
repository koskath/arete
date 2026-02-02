# Slide 18 of Lecture 13 contains information about the CNN Example.

# Here is what the image 1 in slide 18 of lecture 13 contains:

This image illustrates a deep learning neural network architecture with layers visually represented by stacks of rectangles and lines illustrating connections between layers. 

1. **Inputs:**
   - A stack of three dark gray squares labeled "3@32x32," indicating three input channels each with dimensions 32x32.

2. **Convolution (5x5 kernel):**
   - The squares reduce in size and increase in number, forming a stack labeled "Feature maps 32@28x28." This represents 32 feature maps, each 28x28 in size. The squares are connected by lines to the next layer.

3. **Max-pooling (2x2 kernel):**
   - A smaller stack of darker squares labeled "Feature maps 32@18x18," indicating feature maps reduced to 18x18 dimensions. Lines connect these to the subsequent layer.

4. **Convolution (5x5 kernel):**
   - A further reduced stack is labeled "Feature maps 32@10x10," signifying feature maps sized 10x10, connected to the next layer with lines.

5. **Max-pooling (2x2 kernel):**
   - The next stack, smaller in size, is labeled "Feature maps 48@6x6," representing feature maps of 6x6 dimensions. Connections extend to the following layer.

6. **Flatten:**
   - The configuration changes to a flat arrangement labeled "Feature maps 48@4x4," indicating flattening operation. It leads to a straight line connecting to the dense layers.

7. **Fully connected (Hidden units):**
   - Three sets of upward-pointing narrow stacks denote "Hidden units." 
   - The first stack labeled "768," connected to the second labeled "500." Both appear elongated in comparison to previous layers.

8. **Outputs:**
   - Two small squares, suggesting two output units, labeled "Outputs 2."

Each transition between layers is marked by lines, illustrating the flow of data across the network. Labels beneath each configuration specify the type of operation (e.g., "Convolution 5x5 kernel," "Max-pooling 2x2 kernel," "Flatten," and "Fully connected").