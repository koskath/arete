# Here is what the image 1 in slide 23 of lecture 2 contains:

The image shows a screenshot containing Python code and a plot. 

**Code Section:**
- The code is displayed within a light grey cell background.
- The first line of code: `import matplotlib.pyplot as plt` with `import`, `as`, and `plt` highlighted in green.
- The second line of code: `import numpy as np` with `import`, `as`, and `np` highlighted in green.
- The third line of code: `x = np.linspace(0, 10, 100)` with `0`, `10`, and `100` highlighted in orange.
- The fourth line of code: `plt.plot(x, np.sin(x))`.
- The fifth line of code: `plt.plot(x, np.cos(x))`.
- The sixth line of code: `plt.show()`.

**Plot Section:**
- Below the code section, a line plot is displayed.
- The x-axis ranges from 0 to 10, with tick marks and grid lines at intervals of 2 (0, 2, 4, 6, 8, 10).
- The y-axis ranges from -1.00 to 1.00, with tick marks and grid lines at intervals of 0.25 (-1.00, -0.75, -0.50, -0.25, 0, 0.25, 0.50, 0.75, 1.00).
- The plot has two lines:
  - A blue sine wave (\( \sin(x) \)) starting from (0, 0), with peaks at (π/2, 1) and (5π/2, 1), and troughs at (3π/2, -1).
  - An orange cosine wave (\( \cos(x) \)) starting from (0, 1), with peaks at (2π, 1), and troughs at (π, -1).
- Both lines are smoothly interpolated.
- The background of the plot area is light grey, with white grid lines extending across both axes.