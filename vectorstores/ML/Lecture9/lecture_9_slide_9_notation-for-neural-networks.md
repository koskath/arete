# Slide 9 of Lecture 9 contains information about the Notation for Neural Networks.


The slide contains handwritten text, mathematical notations, and a diagram illustrating a model with matrices and arrows. It is organized as follows:

1. **Text at the Top**:
   - The text reads: "We have our usual supervised learning notation:"

2. **Matrix Notation for X and y**:
   - Below the text, two matrices are shown.
   - On the left, a matrix labeled "X" with an equal sign and a bordered matrix:
     - Inside the matrix, entries are vertically listed as \(x_1\), \(x_2\), ..., \(x_n\).
     - A dashed vertical line represents continuation between these rows.
     - The dimensions of the matrix are noted as \(n \times d\) on the bottom right.
   - To the right, a matrix labeled "y":
     - Contains entries \(y_1\), \(y_2\), ..., \(y_n\) vertically.
     - The dimensions noted are \(n \times 1\) on the bottom right.

3. **Text in the Middle**:
   - "We have our latent features:" on the left.
   - "We have two sets of parameters:" on the right.

4. **Matrix Notation for Z, v, and W**:
   - Below the text, three matrices are shown.
   - On the left, a matrix labeled "Z" with an equal sign and a bordered matrix:
     - Entries given as \(z_1\), \(z_2\), ..., \(z_n\) vertically.
     - A dashed line indicates continuation.
     - The dimensions noted are \(n \times K\) on the bottom right.
   - In the middle, a vector labeled "v":
     - Entries shown as \(v_1\), \(v_2\), ..., \(v_K\) vertically inside bordered brackets.
     - The dimensions noted are \(K \times 1\) on the bottom right.
   - On the right, a matrix labeled "W":
     - Entries shown as \(w_1\), \(w_2\), ..., \(w_d\) horizontally inside bordered brackets.
     - Dimensions are \(k \times d\), indicated on the bottom right.

5. **Arrows and Diagram on the Right**:
   - A red arrow extends from "v, W" to a hand-drawn diagram involving nodes and links.
   - The diagram consists of:
     - Three layers of nodes: 
       - Bottom layer has nodes labeled \(x_1, x_2, ..., x_d\).
       - Middle layer has nodes labeled \(z_1, z_2, ..., z_k\).
       - Top node labeled \(y\).
     - Black arrows connect bottom layer nodes to middle layer nodes.
     - Blue arrows connect middle layer nodes to the top node.
   - Parameters \(w_1, w_2, ..., w_k\) are written along connections between the bottom and middle layers.
   - Each blue arrow from the middle to top node is labeled with parameter \(v\).

All elements, annotations, and spatial relationships in the image are captured as described.

Latent or hidden features are computed from observed features using matrix factorization.
CPSC 340: Machine Learning and Data Mining: http://www.stat.yale.edu/Courses/ 1997-98/101/stat101.htm
