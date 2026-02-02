# Here is what the image 1 in slide 22 of lecture 7 contains:

The image consists of two main parts: a text explanation and two plots.

**Text (Top Left):**
- Title: "Outlierness" ratio of example 'i'
- Bullet point: (Avg distance of 'i' to its KNNs)/(Avg distance of neighbors of 'i' to their KNNs)
- Sentence: If outlierness > 1, x is further away from neighbors than expected.

**Plot 1 (Bottom Left):**
- A square scatter plot with multiple black dots.
- Cluster on the upper left labeled "C₁," containing many dispersed black dots.
- Dense cluster on the lower left labeled "C₂," appearing like a small, concentrated group of black dots.
- Two other points labeled: "o₁" on the lower right side near the middle; "o₂" very close to the dense cluster C₂ on the left.

**Plot 2 (Right Side):**
- Scatter plot with axes labeled "Dim. 1" (0 to 100) and "Dim. 2" (0 to 100).
- Plotted points in varying shades of brown, ranging from small dots to larger circled dots.
- Several labeled points with circled borders: 
  - Near (10, 40), number "2.7383" next to a medium circle.
  - Near (40, 20), number "1.358" near a small/medium circle.
  - Near (40, 35), number "1.1967" near a small circle.
  - Near (50, 30), number "1.1184" near a small circle.
  - Around the coordinate (70, 65), a large circle labeled "7.6259."
  - Near (75, 5), circle labeled "5.9645."
  - Near (80, 85), circle labeled "1.2764."
  - At (90, 5), circle labeled "4.1668."
  - Near (90, 35), circles labeled "3.108" and "3.1361."
  - At (92, 90), circle labeled "1.2681."
  - Near (97, 95), small circle labeled "3.4745."
  - Various unlabeled small dots distributed across the plot.
- Larger circles indicate higher "outlierness" values, suggesting they are likely outliers based on the given metric.