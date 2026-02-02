# Slide 37 of Lecture 5 contains information about the Decision Trees.

ASM: Attribute Selection Measure

# Here is what the image 1 in slide 37 of lecture 5 contains:

The image comprises a flowchart illustrating the process of decision tree generation. Here's a detailed description:

1. **Main Flowchart Layout:**
   - The chart is divided into sections with boxes, arrows, and labels, representing different stages of decision tree generation.

2. **Elements from Left to Right:**
   - On the far left, there are two vertically aligned oblong cylinders:
     - The top oblong cylinder is yellow and labeled "Training Data."
     - The bottom oblong cylinder is also yellow and labeled "Test Data."
   - To the left of these cylinders, there's a blue oblong cylinder labeled "Data."

3. **Arrows and Flow:**
   - A black arrow points from "Data" to "Training Data."
   - Another black arrow moves horizontally from "Training Data" into a rectangular box, leading to the process described below.
   - A separate black arrow also moves horizontally from "Test Data" to another box labeled "Model Evaluation."

4. **Decision Tree Generation Box:**
   - A large yellow rectangular box is titled "Decision Tree Generation" at the top.
   - Inside this box are two smaller purple rectangular boxes:
     - The left box is labeled, "Select Best Attribute Using ASM such as Information Gain or Gini Index or Gain Ratio."
     - A black arrow leads from this box right to the second purple box labeled, "Breaks the Dataset into Smaller Subsets."
   - Under the second purple box, there's a text annotation: "Recursively repeat the process for each child," with an arrow pointing back to the arrow leading into the first purple box.

5. **Model Evaluation:**
   - Below the yellow rectangular box, a green rectangular box is labeled "Model Evaluation."
   - A black arrow from the yellow box points downward to this green box.

6. **Performance Evaluation Measures:**
   - To the right of "Model Evaluation," another green box is labeled "Performance Evaluation Measures."
   - It lists the following:
     1. Accuracy
     2. Precision
     3. Recall
   - A black arrow points horizontally from "Model Evaluation" to this box.

The image represents the workflow for generating and evaluating a decision tree, indicating the progression from data input through training data, model evaluation, and performance measures.