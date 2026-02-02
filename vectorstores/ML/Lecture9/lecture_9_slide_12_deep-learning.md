# Slide 12 of Lecture 9 contains information about the Deep Learning.

# Slide Description: *“Deep Learning”*

This slide explains how neural networks become *deep* by stacking multiple hidden layers, and it shows both formulas and a diagram illustrating progressively deeper architectures.

## **Left Side: Mathematical Formulations**

### **1. Linear Model**
Written at the top:
- \( \hat{y}_i = w^\top x_i \)

This represents a simple linear predictor with no hidden layers.

### **2. Neural Network with 1 Hidden Layer**
Formula:
- \( \hat{y}_i = v^\top h(W x_i) \)

Notes:
- The hidden activation is labeled as \( z_i \)
- This corresponds to one layer of nonlinear transformations.

### **3. Neural Network with 2 Hidden Layers**
Formula:
- \( \hat{y}_i = v^\top h\!\left(W^{(2)}\, h(W^{(1)} x_i)\right) \)

Annotations:
- Two nested nonlinear transformations.
- Blue labels indicate:
  - \( z_i^{(1)} \): output of layer 1  
  - \( z_i^{(2)} \): output of layer 2



### **4. Neural Network with 3 Hidden Layers**
Formula:
- \( \hat{y}_i = v^\top h\!\left( W^{(3)}\, h(W^{(2)}\, h(W^{(1)} x_i)) \right) \)

Annotations:
- Three nested nonlinear layers.
- Blue labels:  
  - \( z_i^{(1)} \), \( z_i^{(2)} \), \( z_i^{(3)} \)



### **General Case (m hidden layers)**
Bullet point at the bottom:
- For *m* layers:  
  \( \hat{y}_i = w^\top \left( \prod_{\ell=1}^m h(W^{(\ell)} x_i) \right) \)

### **Important Note (in red):**
- Nonlinearity is essential:  
  - Transform \( z_i \) using activation \( h \)  
  - \( z_i = W x_i \Rightarrow y_i = v^\top h(z_i) \)



## **Right Side: Neural Network Diagram**

A hand-drawn deep neural network with:

### **Input Layer**
- Inputs labeled: \( x_{i1}, x_{i2}, x_{i3}, \dots, x_{id} \)
- These connect upward to the first hidden layer.



### **First Hidden Layer**
- Neurons labeled:  
  \( z_{i1}^{(1)}, z_{i2}^{(1)}, z_{i3}^{(1)}, \dots, z_{ik}^{(1)} \)
- Each neuron outputs a nonlinear activation:  
  \( h(z_{i1}^{(1)}), h(z_{i2}^{(1)}), \dots \)

### **Second Hidden Layer**
- Neurons labeled:  
  \( z_{i1}^{(2)}, z_{i2}^{(2)}, z_{i3}^{(2)}, \dots, z_{ik}^{(2)} \)
- They receive connections from all neurons in layer 1.
- Nonlinear activations shown as:  
  \( h(z_{i1}^{(2)}), h(z_{i2}^{(2)}), \dots \)

Green annotation:
- *“Second layer of latent features”*
- *“You can add more ‘layers’ to go ‘deeper’ ”*


### **Output Neuron**
- Single node at the top labeled \( y_i \)
- Receives connections from all neurons in the last hidden layer.

## **Overall Message of Slide**
- Deeper networks apply repeated nonlinear transformations.
- Each additional layer extracts higher-level *latent features*.
- Deep learning = stacking many hidden layers.




For 'm' layers, we could use multiple layers. Note that non-linearity involves transforming z by a non-linear function 'h': z=Wx ==> y=v h(z).

CPSC 340: Machine Learning and Data Mining: http://www.stat.yale.edu/Courses/ 1997-98/101/stat101.htm
