# Slide 10 of Lecture 12 contains information about De-coupling Hardware and the Plan (“Software”) The “programme” as a hierarchy of plans

## Hierarchical Structure

### Production Planning (Upper Section)

#### Master Production Schedule
Connects to three main planning areas:
- **Forecasting, Rough cut plannig, Delivery date planning**
- **Order processing**

#### Material Requirement Planning (Central Red Box)
Flows to multiple planning functions:
- **Assessment of demand**
- **Order calculation**
- **Inventory accounting**
- **Reservations**

Connects to:
- **Supplier Selection**
- **Purchasing orders writing**
- **Order processing control**

Bidirectional flow between:
- **Shop order** ↔ **Supplier Order**

#### Scheduling and Capacity Planning
Leads to:
- **Lead time scheduling**
- **Capacity requirement planning**

### Production Control (Lower Section)

#### Order Release
Manages:
- **Sequencing**
- **Documents**
- **Job scheduling**

Flows to:
- **Order Release** (execution box)

#### Job Control
Oversees:
- **Expediting, Order progress control**
- **Quantities and deadlines control**
- **Quality control**

Connects to:
- **Incoming goods**
- **Quantities and deadlines**
- **Quality control**

## Key Process Flows
- Gray arrows indicate hierarchical dependencies flowing from left to right
- Blue boxes represent planning and scheduling activities
- Orange/peach boxes represent control and execution activities
- Red box (Material requirement planning) serves as the central planning hub
- Bidirectional arrow between Shop order and Supplier Order indicates coordination