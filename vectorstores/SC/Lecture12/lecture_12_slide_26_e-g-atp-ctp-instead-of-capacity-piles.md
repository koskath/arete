# Slide 26 of Lecture 12 contains information about e.g. ATP, CTP instead of capacity “piles“


- **Special ATP-Functionalities**
  - Online-availability check by managers using different databases  
  - Linked to modules in partner companies  
  - Simulation (what-if, how-to-achieve) to search for alternative solutions  

**Demand: 10 PCs**

**Legend (left side of lower figure):**
- ATP OK  
- Only part  
- ATP OK  
- ATP negative  

_Source: Knollmayer, Figure 3.16: Example for an ATP check_  
_CBS Copenhagen Business School_

## Explanation of the graphs

### **Left graph (capacity piles)**
The left-side diagram shows a histogram-like capacity “pile” visualization. Along the x-axis are numbered time periods (1–8). The y-axis shows capacity utilization in percentages (100%, 200%, 300%).  
Each bar represents available or required capacity for that period. The stacked shading hints at overload in certain periods (bars exceeding 100%, 200%, etc.).  
This illustrates the *traditional* way of planning capacity—using rough aggregate capacity evaluations rather than item-level availability.

### **Right graph (ATP/CTP availability check)**
The lower-right diagram depicts an **ATP (Available-to-Promise)** tree for fulfilling a demand of **10 PCs**.  
It shows components required for final PC assembly (monitor, desktop case, CPU, motherboard, keyboard/mouse, cables, etc.). For each component, availability is indicated by the colored/filled status markers (ATP OK, only partially available, or negative).  

It also shows specific constraints such as:
- “5 assembled motherboards available”
- “No CPUs available”

This illustrates how **ATP/CTP provides detailed, component-level availability checks** across different modules and partner databases. It allows managers to run *what-if simulations* to explore possibilities for fulfilling demand—unlike the simple capacity piles shown on the left.

In essence, the slide contrasts:
- **Old method:** rough capacity piles (limited insight)  
- **New method:** ATP/CTP (precise, component-level availability checks and simulations)

