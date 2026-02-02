# Slide 24 of Lecture 6 contains information about the AUC - ROC Curve.

# Here is what the image 1 in slide 24 of lecture 6 contains:

The image contains two sections, each with Python code and respective ROC curve plots.

**Top Section:**
1. **Code Block:**
   - `plot_roc_curve(y, y_proba)`
   - `print(f'model 1 AUC score: {roc_auc_score(y, y_proba)}')`
   
2. **Text Output:**
   - `model 1 AUC score: 0.5`

3. **Plot:**
   - **Axes:**
     - X-axis labeled "False Positive Rate" ranging from 0.0 to 1.0.
     - Y-axis labeled "True Positive Rate" ranging from 0.0 to 1.0.

   - **Line:**
     - A single blue diagonal line from the bottom-left corner (0.0, 0.0) to the top-right corner (1.0, 1.0).

   - **Plot Characteristics:**
     - The plot is a square with a standard white background and black borders.

**Bottom Section:**
1. **Code Block:**
   - `plot_roc_curve(y, y_proba_2)`
   - `print(f'model 2 AUC score: {roc_auc_score(y, y_proba_2)}')`

2. **Text Output:**
   - `model 2 AUC score: 0.8334048421052631`

3. **Plot:**
   - **Axes:**
     - X-axis labeled "False Positive Rate" ranging from 0.0 to 1.0.
     - Y-axis labeled "True Positive Rate" ranging from 0.0 to 1.0.

   - **Line:**
     - A blue line that starts from the point (0.0, 0.0), initially rises steeply, and then follows a curve with varying upward inclinations, eventually leveling off near the top-right corner at approximately (1.0, 0.833).

   - **Plot Characteristics:**
     - The plot is a square with a standard white background and black borders.