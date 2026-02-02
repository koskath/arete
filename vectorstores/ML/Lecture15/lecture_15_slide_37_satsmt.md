# Slide 37 of Lecture 15 contains information about the SAT/SMT.

SAT-based formal verification represents systems and their desired properties in propositional logic, usually in conjunctive normal form, before an automatic SAT solver checks whether the formula holds. While powerful, these methods struggle with scalability, prompting practitioners to turn to SMT solvers when verifying deep neural networks that involve real or integer parameters, as noted by Shafique et al. in their survey on robust machine learning systems.
