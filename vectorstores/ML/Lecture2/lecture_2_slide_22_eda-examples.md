# Slide 22 of Lecture 2 contains information about the EDA Examples.

The first image uses `sns.FacetGrid(df, hue="species_short", height=5).map(plt.scatter, "culmen_length_mm", "culmen_depth_mm").add_legend()`, 
and the second image relies on `sns.pairplot(df, hue="species_short")` to visualize the data.
