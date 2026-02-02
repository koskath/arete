# Slide 12 of Lecture 11 contains information about the Gated Recurrent Unit (GRU).

# Here is what the image 1 in slide 12 of lecture 11 contains:

The image is a flowchart representation of an LSTM (Long Short-Term Memory) cell, which includes various components and connections, organized as follows:

1. **Input Annotations:**
   - `h_{t-1}` is labeled at the top left as "State vector at previous time instance, t."
   - `x_t` is labeled at the bottom left as "Input at current instance, t."

2. **Input Arrows:**
   - An arrow from `h_{t-1}` points right into an element-wise multiplication circle marked with a green circle, part of the forget gate.
   - Another arrow from `h_{t-1}` bifurcates downwards toward the pink block labeled `W` and the purple box labeled "Forget gate (sigmoid)."
   - An arrow from `x_t` also moves right into the pink block `W`.

3. **Blocks and Gates:**
   - The pink block labeled `W` is centered at the bottom and connects to both the "Forget gate (sigmoid)" and the "Input gate (sigmoid)."
   - The "Forget gate (sigmoid)" is a purple box above and directly links to the element-wise multiplication circle (green) on its right.
   - The "Input gate (sigmoid)" is a yellow box positioned right and above the input `W`, with an arrow leading to an element-wise multiplication circle, and another arrow ascending to the `tanh` function.

4. **Operations:**
   - An orange ellipse labeled `tanh` is present on the right of the "Input gate (sigmoid)," with its output directed towards another green element-wise multiplication circle.
   - This multiplication circle outputs to an element-wise summation circle marked with a red circle on its upper right, which combines outputs from both paths.

5. **Output Arrows:**
   - From the element-wise summation circle, an arrow extends upwards to the top to `y_t`, labeled as "Output at current instance, t."
   - A horizontal arrow from `y_t` moves towards `h_t` at the top right, labeled as "State vector."
   - An arrow loops from `h_t` back to `h_{t-1}` position to indicate recurrence.

6. **Legend:**
   - There is a legend in the bottom right corner explaining symbols used:
     - Green circle for "Element-wise multiplication."
     - Red circle for "Element-wise summation."
     - `h` as "State vector."
   - Additionally, definitions of `h_{t-1}`, `x_t`, and `y_t` are noted as per their corresponding roles.

The arrangement intuitively illustrates the data flow and transformations within an LSTM unit using gates and non-linear transformations.