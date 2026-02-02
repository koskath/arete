# Slide 13 of Lecture 9 contains information about the Activation Functions. (See Bonus Slides for more)
The slide is organized into two columns. The left column features three activation functions: Sigmoid, tanh, and ReLU, each with labels and graphs. The right column displays Leaky ReLU, Maxout, and ELU, each with corresponding labels and graphs or equations.

### Left Column:

1. **Sigmoid:**
   - Label: "Sigmoid" in bold.
   - Formula: \( \sigma(x) = \frac{1}{1 + e^{-x}} \).
   - Graph: A sigmoid curve plotted. The x-axis ranges from -10 to 10, and the y-axis from 0 to 1. The curve starts near 0 for -10, ascends through the origin (0,0.5), and levels off near 1 for 10.

2. **tanh:**
   - Label: "tanh" in bold.
   - Formula: \( \text{tanh}(x) \).
   - Graph: A hyperbolic tangent curve plotted. The x-axis ranges from -10 to 10, and the y-axis from -1 to 1. The curve starts near -1 for -10, crosses the origin, and levels off near 1 for 10.

3. **ReLU:**
   - Label: "ReLU" in bold.
   - Formula: \( \max(0, x) \).
   - Graph: A ReLU function plotted. The x-axis ranges from -10 to 10, and the y-axis from 0 to 10. The function is at 0 for x < 0 and follows y = x for x >= 0.

### Right Column:

1. **Leaky ReLU:**
   - Label: "Leaky ReLU" in bold.
   - Formula: \( \max(0.1x, x) \).
   - Graph: A Leaky ReLU function plotted. The x-axis ranges from -10 to 10, and the y-axis from -1 to 10. The graph has a small positive slope for x < 0 and follows y = x for x >= 0.

2. **Maxout:**
   - Label: "Maxout" in bold.
   - Formula: \( \max(w_1^Tx + b_1, w_2^Tx + b_2) \).
   - No graph is associated with this function, only the formula is displayed.

3. **ELU:**
   - Label: "ELU" in bold.
   - Formula: 
     - \{
       \( x \),  \( x \geq 0 \),
       \( \alpha(e^x - 1) \), \( x < 0 \).
   - Graph: An ELU function plotted. The x-axis ranges from -10 to 10, and the y-axis from -2 to 10. The graph shows a gentle curve for x < 0 and follows y = x for x >= 0.

Each section is well-organized with consistent formatting, including bold font for titles and appropriate alignment of formulas and graphs. Graphs use blue lines with labeled axes.
