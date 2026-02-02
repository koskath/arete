# Slide 14 of Lecture 6 contains information about the SVM: Nonlinear Data.

For nonlinear data, you can add a new dimension z defined by the rule z = x^2 + y^2, turning a circular decision boundary of radius 1 in the original 2D space into a plane parallel to the x-axis at z = 1 in 3D, where SVM can then find a linear hyperplane that cleanly separates the two linearly separable groups.

# Here is what the image 1 in slide 14 of lecture 6 contains:

The image consists of four panels arranged horizontally, each featuring a plot with annotations and descriptive text below.

**First Panel:**
- A 2D scatter plot with axes labeled "x" (horizontal) and "y" (vertical).
- Blue circles clustered centrally and red triangles scattered around periphery.
- Axes intersect at origin marked "0."
- Below the panel, text reads:
  - "Add z dimension"
  - "Rule: z = x² + y²"

**Second Panel:**
- A 2D plot simulating 3D view with "x" (horizontal) and "z" (vertical) axes.
- Blue circles clustered near origin on x-axis; red triangles spread higher on z-axis.
- Text below reads:
  - "Data in two linearly separated groups"

**Third Panel:**
- Similar 2D plot with "x" (horizontal) and "z" (vertical) axes.
- Blue circles remain near origin; red triangles higher on z-axis.
- Bold horizontal line labeled "Best hyperplane" near the bottom.
- Below, text reads:
  - "In 3D, hyperplane is a plane parallel to x axis at a certain z (z = 1)."

**Fourth Panel:**
- A 2D scatter plot, axes labeled "x" (horizontal) and "y" (vertical).
- Blue circles in center, surrounded by circular boundary, labeled "Best hyperplane."
- Red triangles remain outside boundary on periphery.
- Text beneath reads:
  - "Decision boundary is a circumference of radius 1 (separates both tags using SVM)"