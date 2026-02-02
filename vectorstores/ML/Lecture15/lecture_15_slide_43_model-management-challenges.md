# Slide 43 of Lecture 15 contains information about the Model Management Challenges.

Model management presents challenges at multiple stages. Defining the model can be difficult because input data must be transformed into the exact features a model expects, and machine learning pipelines often bundle feature transformations with the core model into a single abstraction. Validation adds another layer of complexity: teams need the ability to back-test models over time—especially after updates—by reusing the same training, test, and validation sets as well as consistent evaluation metrics.

Retraining decisions are equally fraught. Although training typically occurs offline with models loaded at prediction time, real-world events such as new public holidays or promotional campaigns can introduce patterns unseen during training, requiring teams to trigger retraining or even redesign the model to maintain performance.
