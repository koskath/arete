# Slide 26 of Lecture 15 contains information about the What is AI alignment?.

AI alignment is the process of encoding human values and goals into large language models so they behave in helpful, safe, and reliable ways, enabling enterprises to tailor models to their own business rules and policies. Alignment generally occurs during fine-tuning, where a foundation model is fed task-specific examples that steer its behavior toward the desired outcomes.

The workflow typically involves two steps. During instruction tuning, the model receives curated examples of the target task and learns by imitation. In the critique phase, a human or another AI system interacts with the model and evaluates its responses in real time; in reinforcement learning contexts this feedback loop is commonly referred to as RLHF when humans grade the outputs or RLAIF when AI systems provide the critiques.
