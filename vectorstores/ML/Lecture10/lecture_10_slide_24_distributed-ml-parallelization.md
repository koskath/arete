# Slide 24 of Lecture 10 contains information about the Distributed ML: Parallelization.

Parallelization methods in deep learning include data, model, and pipeline strategies as well as hybrids that mix elements of each, providing flexibility for different workloads and hardware constraints.

In data parallelism, multiple machines load identical copies of the model, split the training data into non-overlapping chunks, and feed those chunks to their local replicas so each worker updates parameters based on its subset; afterward, the model parameters must be synchronized across workers to keep the replicas aligned, a process detailed by Mayer, Ruben, and Hans-Arno Jacobsen in “Scalable deep learning on distributed infrastructures: Challenges, techniques, and tools,” ACM Computing Surveys (CSUR) 53.1 (2020): 1–37.
