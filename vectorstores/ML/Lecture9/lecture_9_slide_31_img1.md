# Here is what the image 1 in slide 31 of lecture 9 contains:

The image contains text and a diagram related to neural networks and deep learning.

**Text Section (Left Top to Bottom):**

1. "Linear model: ŷᵢ = wᵀxᵢ"
2. "Neural network with 1 hidden layer: ŷᵢ = vᵀh(Wxᵢ)"
   - Annotation below formula: "zᵢ"
3. "Neural network with 2 hidden layers: ŷᵢ = vᵀh(W⁽²⁾h(W⁽¹⁾xᵢ))"
   - Annotations below formula: "zᵢ⁽¹⁾", "zᵢ⁽²⁾"
4. "Neural network with 3 hidden layers: ŷᵢ = vᵀh(W⁽³⁾h(W⁽²⁾h(W⁽¹⁾xᵢ)))"
   - Annotations below formula: "zᵢ⁽¹⁾", "zᵢ⁽²⁾", "zᵢ⁽³⁾"

**Text Section (Right):**

- Blue text at top: "Deep learning"
- Green text alongside arrows: "Second 'layer' of latent features", "You can add more 'layers' to go 'deeper'"

**Diagram (Right):**

- Three layers of nodes connected by arrows.
- Top layer: three nodes labeled "h(zᵢ₁⁽²⁾)", "h(zᵢ₂⁽²⁾)", "h(zᵢ₃⁽²⁾)", with horizontal ellipsis indicating continuation, all connected upwards to a node labeled "ŷᵢ".
- Middle layer: three nodes labeled "zᵢ₁⁽²⁾", "zᵢ₂⁽²⁾", "zᵢ₃⁽²⁾", with horizontal ellipsis indicating continuation.
- Bottom layer: four nodes labeled "h(zᵢ₁⁽¹⁾)", "h(zᵢ₂⁽¹⁾)", "h(zᵢ₃⁽¹⁾)", "h(zᵢₖ⁽¹⁾)".
- First and middle layers connected by black arrows; middle and top layers connected by blue arrows.
- Input nodes at bottom labeled "xᵢ₁", "xᵢ₂", "xᵢ₃", "xᵢd".
- Nodes at level "z⁽¹⁾" and input nodes connected by black arrows.