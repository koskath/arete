# Slide 11 of Lecture 9 contains information about the Why “Neural Network”?.

The slide visually explains why artificial neural networks are named after biological neural systems.

## **Left Side: Biological Neuron Diagram**
A labeled sketch of a **nerve cell (neuron)** showing:
- **Dendrites** (branch-like structures receiving signals)
- **Nucleus**
- **Cell body**
- **Axon** with **myelin sheath**
- **Schwann cells**
- **Nodes of Ranvier**
- **Axon terminals / synaptic bulbs**
- **Synapse**
- **Dendrite of next neuron**

This biological neuron illustration is connected by a red arrow to the artificial neural network on the right.

---

## **Right Side: Artificial Neural Network Diagram**
A hand-drawn multilayer neural network with input, hidden, and output layers.

### **Input Layer**
- Nodes labeled `x_i1, x_i2, x_i3, …, x_id`
- Incoming arrows lead to hidden-layer neurons.
- Notes refer to these as **“dendrites”** for the artificial neuron `z_ik`, receiving the input values `x_ij`.

### **Hidden Layer**
- Neurons labeled `z_i1, z_i2, z_i3, …, z_ik`
- Outputs are passed through activation functions: `h(z_i1), h(z_i2), …`
- Arrows go upward to the output neuron.
- Notes explain:
  - A neuron **aggregates signals** using `w_c^T x_i`
  - A **binary signal** `h(w_c^T x_i)` is sent along an artificial **“axon”**

### **Output Layer**
- A single neuron labeled `y_i`
- Its output is computed by aggregating:  
  **`v^T h(W x_i)`**
- Notes mention:
  - **Predictions** are based on this aggregation at the output “neuron”
  - A **synapse** exists between hidden neuron outputs `z_ik` and the output neuron `y_i`

---

## **Annotations (in blue handwriting)**
The slide uses biological analogies:
- *“Predictions based on aggregation \( v^T h(W x_i) \) at \( y_i \) neuron”*
- *“Synapse between \( z_{i k} \) and \( y_i \) neuron”*
- *“Binary signal \( h(w_c^T x_i) \) sent along axon”*
- *“Neuron aggregates signals: \( w_c^T x_i \)”*
- *“Dendrites for \( z_{i k} \) neuron are receiving \( x_{ij} \) values”*

---

## **Bottom Right**
- Slide number **13**

The entire slide emphasizes the parallel between **biological neurons** and **artificial neural networks**, motivating the terminology used in machine learning.
