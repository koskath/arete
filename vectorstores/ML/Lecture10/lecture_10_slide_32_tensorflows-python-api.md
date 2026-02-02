# Slide 32 of Lecture 10 contains information about the TensorFlow’s Python API.

At the lowest level, each TensorFlow operation is implemented in C++, and many operations offer multiple implementations called kernels, each optimized for specific devices such as CPUs, GPUs, or TPUs.

GPUs speed up computation by splitting workloads into many smaller chunks that run in parallel, while TPUs are custom ASIC chips built specifically for deep-learning operations.
