# Here is what the image 1 in slide 35 of lecture 10 contains:

The image is a flowchart or diagram illustrating a process involving tensors. 

- There are four rectangular boxes on the left side, each with a single word label. From top to bottom, these are:
  1. "biases"
  2. "weights"
  3. "examples"
  4. "labels"
  
- There are four oval shapes arranged horizontally from left to right, each labeled with a single word:
  1. "MatMul"
  2. "Add"
  3. "Relu"
  4. "Xent"
  
- Arrows connect the shapes and boxes, indicating the flow of the process:
  1. Arrows originating from "biases" and pointing to "Add".
  2. An arrow originating from "weights" and pointing to "MatMul".
  3. An arrow from "examples" pointing to "MatMul".
  4. An arrow from "labels" pointing to "Xent".
  5. An arrow from "MatMul" pointing to "Add".
  6. An arrow from "Add" pointing to "Relu".
  7. An arrow from "Relu" pointing to "Xent".
  
- The arrows are thick and red with arrowheads to indicate direction.

- In the top right corner, there is a textual annotation: "Edges are N-dimensional arrays: Tensors," in black font.

This diagram likely represents a basic neural network operation flow involving matrix multiplication, addition, activation, and cross-entropy calculation, with inputs as tensors.