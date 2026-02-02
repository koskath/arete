# Slide 16 of Lecture 9 contains information about the Adding Bias.

# Here is what the image 1 in slide 16 of lecture 9 contains:

The image contains two sections representing different neural network structures. 

**Left Section: Linear Model with Bias**
- Title: "Linear model with bias" written above the diagram.
- Oval labeled "1" at the leftmost side with an arrow pointing right towards the central node.
- Four ovals labeled: \( x_{i1} \), \( x_{i2} \), \( x_{i3} \), followed by "...", \( x_{in} \), each having an upward arrow pointing towards the central oval.
- Central oval labeled \( y_i \) with arrows pointing back to each of the input ovals, indicating incoming connections. 
- All arrows in this section are black, except for one blue arrow originating from the "1" oval pointing directly to \( y_i \).

**Right Section: Multilayer Neural Network with Bias**
- Topmost row: An oval labeled \( y_i \) in the top center. Arrows are pointing to it from intermediate level nodes.
- Second row from the top: Five ovals labeled \( h(z_{i1}^{(2)}) \), \( h(z_{i2}^{(2)}) \), \( h(z_{i3}^{(2)}) \), continuing with "...", \( h(z_{ik}^{(2)}) \). Each has an upward arrow pointing to \( y_i \) and a downward arrow from the previous layer.
- Third row: Five ovals labeled \( z_{i1}^{(2)} \), \( z_{i2}^{(2)} \), \( z_{i3}^{(2)} \), continuing with "...", \( z_{ik}^{(2)} \). Arrows point to the intermediate layer above and originate from the layer below.
- Fourth row: Five ovals labeled \( h(z_{i1}^{(1)}) \), \( h(z_{i2}^{(1)}) \), \( h(z_{i3}^{(1)}) \), continuing with "...", \( h(z_{ik}^{(1)}) \). Each connects to the layer above and is connected to the values in the row below.
- Fifth row: Five ovals labeled \( z_{i1}^{(1)} \), \( z_{i2}^{(1)} \), \( z_{i3}^{(1)} \), continuing with "...", \( z_{ik}^{(1)} \). Arrows indicate connections to the intermediate layers above and are fed from bottom inputs.
- Bottommost row: Oval labeled "1" on the left. Five sequential ovals labeled \( x_{i1} \), \( x_{i2} \), \( x_{i3} \), continuing with "...", \( x_{id} \).
- Blue arrows originate from oval labeled "1" on the bottom left, connecting to the intermediate ovals in the first and second \( z \) layers.
- Black connections depict neural pathways across different layers moving from the bottommost input row up to the output labeled \( y_i \).

# Here is what the image 2 in slide 16 of lecture 9 contains:

The image depicts a neural network diagram consisting of three layers: input layer, hidden layer, and output layer. The input layer contains three nodes. The first node on the left is a yellow circle labeled "1," which connects with outgoing arrows to all nodes in the hidden layer. The next two nodes are green circles, labeled "x₁" and "x₂," respectively, each with an arrow pointing upwards, also connecting to all nodes in the hidden layer.

The hidden layer consists of four nodes. These nodes are blue circles with a depicted sum-of-products symbol inside, featuring a sigma "Σ" symbol at the top and bottom in a stacked fashion. Each node in the hidden layer has incoming arrows from all nodes in the input layer and outgoing arrows leading to each node in the output layer.

The output layer has three nodes, each represented as a blue circle similar to the hidden layer nodes, with the same sum-of-products symbols inside. There are arrows pointing from each node in the hidden layer to every node in the output layer. Additionally, each node in the output layer has an outgoing arrow extending upwards without connecting to any further structure.

Arrows interconnect the layers progressively from the input to the hidden and from the hidden to the output layer. Three dashed bracketed annotations run vertically parallel to the layers on the right side of the diagram, labeled as follows from top to bottom: "Output layer," "Hidden layer," and "Input layer."