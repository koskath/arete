# Slide 60 of Lecture 7 contains information about the SMOTE vs ADASYN.

from imblearn import FunctionSampler # to use a idendity sampler
from imblearn.over_sampling import ADASYN, SMOTE
X, y = create_dataset(n_samples=150, weights=(0.1, 0.2, 0.7))
fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(15, 15))
samplers = [
FunctionSampler(),
RandomOverSampler(random_state=0),
SMOTE(random_state=0),
ADASYN(random_state=0),
]
for ax, sampler in zip(axs.ravel(), samplers):
title = "Original dataset" if isinstance(sampler, FunctionSampler) else None
plot_resampling(X, y, sampler, ax, title=title)
fig.tight_layout() • SMOTE will not make • Focus on samples
any distinction. which are difficult to
classify with a nearest-
neighbors rule.
https://imbalanced-learn.org/stable/auto_examples/over-sampling/plot_comparison_over_sampling.html#sphx-glr-auto-examples-over-sampling-plot-comparison-over-sampling-py
