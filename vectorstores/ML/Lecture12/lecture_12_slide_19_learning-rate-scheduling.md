# Slide 19 of Lecture 12 contains information about the Learning Rate Scheduling.

A well-chosen learning rate is critical: set it too high and training can diverge, but set it too low and convergence takes an impractically long time. One effective heuristic trains the model for a few hundred iterations while exponentially increasing the learning rate from a tiny value to a large one; by inspecting the resulting learning curve, you select a rate just below the point where the loss spikes, reinitialize the model, and train using that rate. 
