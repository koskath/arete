# Here is what the image 1 in slide 46 of lecture 1 contains:

## Evolving From ML-Based Programming to an Automated ML Pipeline

The image shows how a basic machine-learning workflow can evolve into a more automated and scalable pipeline.

---

### **Left Side: Standard ML-Based Programming**
This repeats the workflow from the previous slide:

1. **Study the problem**  
   Understand the task and requirements.

2. **Collect/prepare data**  
   Data points (shown as dots on a plot) are used for learning.

3. **Train ML algorithm**  
   A model is trained on the available data.

4. **Evaluate solution**  
   - Good performance → 😊 **Launch!**  
   - Bad performance → ☹️ **Analyze errors**

5. **Analyze errors**  
   Identify issues with data, model choice, features, etc.

6. Loop continues until performance is acceptable.

---

### **Right Side: Toward Automated ML Pipelines**

The right diagram shows a more advanced and partially **automated ML lifecycle**:

1. **Data**  
   New or additional data is incorporated continuously.

2. **Update data**  
   The dataset can be automatically refreshed (e.g., new user interactions, logs, sensor data).

3. **Train ML algorithm**  
   Model retraining can occur automatically when data changes.

4. **Evaluate solution**  
   Performance is assessed on validation/test metrics.  
   - If the model passes → 😊 **Launch!**  
   - If it fails → the loop continues.

5. **Automation Loop**  
   An oval labeled *“Can be automated”* highlights that:
   - Data updating  
   - Model training  
   - Evaluation  
   can all be part of an automated pipeline (e.g., MLOps, continuous training).

---

### **Key Idea**
The diagram illustrates the progression from **manual, iterative ML development** to **automated, continuous ML workflows**, enabling scalable and repeatable machine-learning systems.
