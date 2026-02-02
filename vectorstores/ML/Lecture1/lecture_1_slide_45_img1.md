# Here is what the image 1 in slide 45 of lecture 1 contains:

## Traditional Programming vs. ML-Based Programming

The image contrasts two development workflows:

---

### **Traditional Programming**
1. **Study the problem**  
   Developers analyze the task and determine what rules are needed.

2. **Write rules**  
   Domain experts manually encode logic (highlighted in pink in the diagram).

3. **Evaluate**  
   The program is tested.  
   - If it performs well → 😊 **Launch!**  
   - If it performs poorly → ☹️ **Analyze errors**

4. **Analyze errors**  
   Developers inspect failures and adjust their hand-written rules.

5. The cycle repeats until the system performs satisfactorily.

---

### **Machine-Learning–Based Programming**
1. **Study the problem**  
   Similar starting point: understand the task.

2. **Gather or load data**  
   Data (shown as points on a graph) becomes the core ingredient for learning.

3. **Train an ML algorithm**  
   Instead of manually writing rules, a model learns patterns from the data.

4. **Evaluate solution**  
   - If performance is good → 😊 **Launch!**  
   - If performance is poor → ☹️ **Analyze errors**

5. **Analyze errors**  
   Instead of rewriting rules, practitioners examine data issues, model design, and evaluation metrics, then improve the dataset or model.

6. The cycle repeats until the model is good enough to deploy.

---

### **Key Difference**
- **Traditional programming**: rules are *explicitly coded by humans*.  
- **ML-based programming**: rules are *learned from data* via model training.

