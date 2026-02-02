# Slide 12 of Lecture 12 contains information about Planning the quantities - Requirement planning: Primary/Secondary - Gross/net requirements

# The image 1 in slide 12 of lecture 12 contains a text document structured as an indented bill of materials (BOM) for a product labeled "1605 Snow Shovel". The layout includes descriptions, component numbers, names, and quantities required, organized hierarchically.

1. Title:
   - "Indented bill of materials (BOM)"

2. Product:
   - "1605 Snow Shovel"

3. Components and Indentations:
   - **13122**: "Top Handle Assembly (1 required)"
     - Indented under it:
       - **457**: "Top Handle (1 required)"
       - **082**: "Nail (2 required)"
       - **11495**: "Bracket Assembly (1 required)"
         - Double-indented under it:
           - **129**: "Top Handle Bracket (1 required)"
           - **1118**: "Top Handle Coupling (1 required)"
   - **048**: "Scoop-Shaft Connector (1 required)"
     - Indented under it:
       - **118**: "Shaft (1 required)"
       - **082**: "Nail (2 required)"
       - **14127**: "Rivet (4 required)"
   - **314**: "Scoop Assembly"
     - Indented under it:
       - **2142**: "Scoop (1 required)"
       - **019**: "Blade (1 required)"
       - **14127**: "Rivet (6 required)"

Each component number is followed by its description and the quantity required within parentheses, with varying indentation levels to indicate hierarchical relationships. The indentation visually represents sub-assemblies or parts that are part of larger assemblies.


# The figure 2.5 in slide 12 of lecture 12 contains a structured table with multiple columns and rows, which details the gross and net requirement calculations for the snow shovel. The components of the table are as follows:

- **Column Headers**:
  - "Part description"
  - "Part number"
  - "Inventory"
  - "Scheduled receipts"
  - "Gross requirements"
  - "Net requirements"

- **Row Entries**:
  1. **Top handle assembly**
     - Part number: 13122
     - Inventory: 25
     - Scheduled receipts: —
     - Gross requirements: 100
     - Net requirements: (connected downwards with an arrow to nodes labeled 75, 75)
  2. **Top handle**
     - Part number: 457
     - Inventory: 22
     - Scheduled receipts: 25
     - Gross requirements: (originates from 75 node with an arrow)
     - Net requirements: 28
  3. **Nail (2 required)**
     - Part number: 082
     - Inventory: 4
     - Scheduled receipts: 50
     - Gross requirements: 150
     - Net requirements: 96
  4. **Bracket assembly**
     - Part number: 11495
     - Inventory: 27
     - Scheduled receipts: —
     - Gross requirements: (originates from 75 node, positioned below Top handle line)
     - Net requirements: 48
  5. **Top handle bracket**
     - Part number: 129
     - Inventory: 15
     - Scheduled receipts: —
     - Gross requirements: (connected to node labeled 48, positioned below Bracket assembly line)
     - Net requirements: 33
  6. **Top handle coupling**
     - Part number: 1118
     - Inventory: 39
     - Scheduled receipts: 15
     - Gross requirements: (connected from node labeled 48)
     - Net requirements: —

- **Annotations**:
  - Lines and arrows are used to show relationships between the "Gross requirements" and "Net requirements" across rows. There are arrows pointing downward from the numbers 75 and 48 in "Gross requirements" to their respective "Net requirements" entries in subsequent rows.

- **Stylistic Elements**:
  - The text is formatted in a tabular structure with horizontal separations between the header and data entries.
  - There is a horizontal line above the headers and another below "Figure 2.5" in the top left corner of the image.

These details form a hierarchical representation of data related to snow shovel components, focusing on inventory and calculation aspects.