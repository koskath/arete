# Here is what the image 1 in slide 37 of lecture 15 contains:

The image contains a block diagram with three main rectangular sections connected by arrows, organized horizontally from left to right. 

1. **Left Section (Program):**
   - Enclosed in a rectangular box with two segments: the top section with code and the bottom labeled section.
   - **Top Section:** 
     - The text includes two scanf statements:
       - `scanf("%d", a);`
       - `scanf("%d", b);`
     - Followed by an if-else construct written as:
       - `if (a > b)`
       - `c = a/b;`
       - `else`
       - `c = b/a;`
     - The keywords `if` and `else` are highlighted in blue.
   - **Bottom Section:**
     - Contains the word “Program” in bold, black font, centered, and placed inside a light gray background.

2. **Middle Section (Constraints):**
   - Contains two vertically stacked rectangular boxes, each with a distinct label on a colored background.
   - **Top Box (Program Constraints):**
     - Light green background.
     - Inside are two logical expressions separated by a disjunction symbol `∨`:
       - `{ (a>b) ∧ (c=a/b) } ∨ { ~(a>b) ∧ (c=b/a) }`
     - Labeled at the top with “Program Constraints” in black font.
   - **Bottom Box (Property Constraints):**
     - Light blue background.
     - Contains a single logical expression:
       - `~(a=0) ∧ ~(b=0) ∧ (c>=1)`
     - Labeled at the top with “Property Constraints” in black font.
   - Black arrows connect each of the constraint boxes to the rightmost section.

3. **Right Section (CNF):**
   - A larger rectangle containing a complex list of expressions.
   - Contains four main disjunctive expressions in the form of logical operations combined with `∧`:
     - `{ (a>b) ∨ ~(a>b) } ∧`
     - `{ (a>b) ∨ (c=b/a) } ∧`
     - `{ (c=a/b) ∨ ~(a>b) } ∧`
     - `{ (c=a/b) ∨ (c=b/a) } ∧`
   - Followed by a single line:
     - `((a=0) ∨ (b=0) ∨ ~(c>=1))`
   - The bottom contains the label “CNF” in bold black font on a light gray background.

Each section is demarcated with solid black borders. Arrows move horizontally from the left “Program” section to their respective constraint boxes, then to the final “CNF” section.