# Slide 11 of Lecture 11 contains information about the LSTM VS GRU.

# Here is what the image 1 in slide 11 of lecture 11 contains:

The image depicts two diagrams representing the architecture of Long Short-Term Memory (LSTM) networks. Each diagram is enclosed in a rectangular boundary, indicating the LSTM cell structure.

### Left Diagram:
- **Input and Outputs:** 
  - On the left, an arrow labeled \( C_{t-1} \) enters the box.
  - On the top, \( y_t \) points upwards, and on the right, arrows labeled \( C_t \) and \( h_t \) exit the box.

- **Gates and Processes:**
  - A purple rectangular box labeled "Forget gate (sigmoid)" with an input arrow feeding into it, connects to a multiplication node (depicted as a circle with a multiplication symbol inside).
  - An orange rectangular box labeled "Gate to control input gate (tanh)" connects to another orange rectangular box labeled "Input gate (sigmoid)," which feeds into the same multiplication node.
  - The resulting product from this multiplication node connects to a summation node (depicted as a circle with a plus sign inside). The input to this node also comes directly from \( C_{t-1} \) after passing through the initial multiplication node.
  - Another path connects to a Tanh function (depicted as an orange oval labeled "tanh"), which feeds into an additional multiplication node.
  - A blue rectangular box labeled "Output gate (sigmoid)" receives input, connecting to a multiplication node between \( h_t \) and \( y_t \).

### Right Diagram:
- **Input and Outputs:**
  - An arrow labeled \( h_{t-1} \) enters from the left side.
  - On the top, \( y_t \) points upwards, and an arrow labeled \( h_t \) exits on the right side.

- **Gates and Processes:**
  - A purple rectangular box labeled "Forget gate (sigmoid)" with an input arrow feeds into a multiplication node.
  - The multiplication node outputs to an addition node (depicted as a circle with a plus sign).
  - A yellow circular function labeled "σ" (sigma) connects to an orange rectangular box labeled "Input gate (sigmoid)"—both feeding into another multiplication node.
  - The path includes a line diving from the previous multiplication to another multiplication node, which connects with a Tanh function (depicted as an orange oval).
  - The output of the tanh function feeds into the final multiplication node leading to the output \( h_t \).

### General Elements:
- **Color-Coded Gates and Nodes:**
  - Forget gates are in purple.
  - Input gates are in orange.
  - Output gates are in blue.
  - Tanh functions are in oval shapes, colored orange.
  - Multiplication nodes are circles with green outlines and contain multiplication signs.
  - Addition nodes are circles with red outlines and contain plus signs.

Both diagrams contain lines and arrows denoting the flow of information and processes within the LSTM cell. The elements are arranged linearly with inputs on the left, processes in the middle, and outputs on the right.
