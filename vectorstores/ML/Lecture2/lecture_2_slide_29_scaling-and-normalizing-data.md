# Slide 29 of Lecture 2 contains information about the Scaling and Normalizing Data.

Some learning algorithms are sensitive to differences in variable scales, such as when one feature ranges from 0 to 1 but another spans 100 to 10,000, so the data can be scaled (for example to the range 0–1 with `sklearn.preprocessing.MinMaxScaler()`), standardized to express measurements as σ from the mean using `sklearn.preprocessing.StandardScaler()`, or log transformed.
