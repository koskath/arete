# Slide 16 of Lecture 13 contains information about the Convolution Layer Training Process.

# Here is what the image 1 in slide 16 of lecture 13 contains:

The image is divided into two main sections labeled "Forward Propagation" on the left and "Backpropagation" on the right.

**Left Section (Forward Propagation):**
1. **Nodes and Connections:**
   - Six cyan circular nodes arranged vertically on the left.
   - Three magenta circular nodes in the middle.
   - Two brown circular nodes on the right.
   - Connections:
     - Each cyan node is connected to each magenta node with colored lines: blue, orange, red, green, yellow.
     - Each magenta node is connected to a brown node with bold black arrows.

2. **Annotations:**
   - Title "Forward Propagation" at the top.
   - A legend at the bottom left:
     - "Input Feature Map" represented by a cyan and blue grid.
     - "Kernel" represented by a square divided into four colors: red, green, yellow, and blue.
     - "Conv." represented by a magenta square.
     - "Pool" represented by a brown rectangle.

**Right Section (Backpropagation):**
1. **Nodes and Connections:**
   - Similar arrangement of nodes as in the left section: six cyan, three magenta, and two brown.
   - Connections:
     - Each magenta node is connected back to each cyan node with colored arrows: blue, orange, red, yellow, green.
     - The magenta nodes have labels: δ₁₁, δ₁₂, δ₂₁, δ₂₂, located in gray boxes next to each node.
     - The brown nodes are connected to the magenta nodes with black arrows.

2. **Annotations:**
   - Title "Backpropagation" at the top.
   - In the center in large red text: "No learning takes place on the pooling layers!!"
   - A legend at the bottom right:
     - "Input Feature Map" is the same grid as left.
     - "Gradients at Conv." is represented by a square divided into four sections labeled δ₁₁, δ₁₂, δ₂₁, δ₂₂.
     - "Kernel" represented similarly as before with four colors.
     - "Pool" with a brown rectangle.
   - An additional diagram showing "Kernel Flipped 180°" pointing from a square of four colors to an identical square orientation.
   - At the bottom, the text "Gradients ==> δ₁₁, δ₁₂, δ₂₁, δ₂₂."

The nodes, connections, legends, and annotations provide a detailed representation of the processes of forward propagation and backpropagation with emphasis on the pooling aspect.

The convolutional layer training process alternates forward propagation, which computes activations, with backpropagation, which passes gradients—denoted δ₁₁, δ₁₂, δ₂₁, δ₂₂, and so on—through the network to update convolutional filters, while pooling layers simply forward values and do not learn separate parameters. 