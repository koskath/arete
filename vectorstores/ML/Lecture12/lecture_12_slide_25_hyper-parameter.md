# Slide 25 of Lecture 12 contains a table with information about the Hyper-parameter Optimization Techniques.

The image displays a table comparing common HPO (Hyperparameter Optimization) algorithms. The table consists of four columns: 

1. **HPO Method**
2. **Strengths**
3. **Limitations**
4. **Time Complexity**

The table includes rows for different HPO methods with corresponding strengths, limitations, and time complexity values.

- **Row 1:**
  - HPO Method: GS
  - Strengths: 
    - Simple.
  - Limitations: 
    - Time-consuming 
    - Only efficient with categorical HPs.
  - Time Complexity: \(O(n^k)\)

- **Row 2:**
  - HPO Method: RS
  - Strengths: 
    - More efficient than GS
    - Enable parallelization.
  - Limitations: 
    - Not consider previous results 
    - Not efficient with conditional HPs.
  - Time Complexity: \(O(n)\)

- **Gradient-based models:**

  - **Row 3:**
    - HPO Method: BO-GP
    - Strengths: 
      - Fast convergence speed for continuous HPs.
    - Limitations: 
      - Only support continuous HPs.
      - May only detect local optimums.
    - Time Complexity: \(O(n^k)\)

- **Row 4:**
  - HPO Method: SMAC
  - Strengths:
    - Efficient with all types of HPs.
  - Limitations:
    - Poor capacity for parallelization.
  - Time Complexity: \(O(n\log n)\)

- **Row 5:**
  - HPO Method: BO-TPE
  - Strengths:
    - Efficient with all types of HPs.
    - Keep conditional dependencies.
  - Limitations:
    - Poor capacity for parallelization.
  - Time Complexity: \(O(n\log n)\)

- **Hyperband:**
  - **Row 6:**
    - Strengths:
      - Enable parallelization.
    - Limitations:
      - Not efficient with conditional HPs.
      - Require subsets with small budgets to be representative.
    - Time Complexity: \(O(n\log n)\)

- **Row 7:**
  - HPO Method: BOHB
  - Strengths:
    - Efficient with all types of HPs.
    - Enable parallelization.
  - Limitations:
    - Require subsets with small budgets to be representative.
  - Time Complexity: \(O(n\log n)\)

- **Row 8:**
  - HPO Method: GA
  - Strengths:
    - Efficient with all types of HPs.
    - Not require good initialization.
  - Limitations:
    - Poor capacity for parallelization.
  - Time Complexity: \(O(n^2)\)

- **Row 9:**
  - HPO Method: PSO
  - Strengths:
    - Efficient with all types of HPs.
    - Enable parallelization.
  - Limitations:
    - Require proper initialization.
  - Time Complexity: \(O(n\log n)\)

Above the table, there is a descriptive text: "The comparison of common HPO algorithms (n is the number of hyper-parameter values and k is the number of hyper-parameters)."