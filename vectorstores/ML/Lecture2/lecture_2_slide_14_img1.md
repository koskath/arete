# Here is what the image 1 in slide 14 of lecture 2 contains:

The image shows a table with seven columns and five rows, including the header row. The columns are labeled from left to right as follows: "species_short," "island," "culmen_length_mm," "culmen_depth_mm," "flipper_length_mm," "body_mass_g," and "sex."

- Row 0:
  - species_short: "Adelie"
  - island: "Torgersen"
  - culmen_length_mm: "39.100"
  - culmen_depth_mm: "18.700"
  - flipper_length_mm: "181.000"
  - body_mass_g: "3750.000"
  - sex: "MALE"

- Row 1:
  - species_short: "Adelie"
  - island: "Torgersen"
  - culmen_length_mm: "39.500"
  - culmen_depth_mm: "17.400"
  - flipper_length_mm: "186.000"
  - body_mass_g: "3800.000"
  - sex: "FEMALE"

- Row 2:
  - species_short: "Adelie"
  - island: "Torgersen"
  - culmen_length_mm: "40.300"
  - culmen_depth_mm: "18.000"
  - flipper_length_mm: "195.000"
  - body_mass_g: "3250.000"
  - sex: "FEMALE"

- Row 3 (highlighted with a dashed red rectangle):
  - species_short: "Adelie"
  - island: "Torgersen"
  - culmen_length_mm: "nan"
  - culmen_depth_mm: "nan"
  - flipper_length_mm: "nan"
  - body_mass_g: "nan"
  - sex: "NaN"

- Row 4:
  - species_short: "Adelie"
  - island: "Torgersen"
  - culmen_length_mm: "36.700"
  - culmen_depth_mm: "19.300"
  - flipper_length_mm: "193.000"
  - body_mass_g: "3450.000"
  - sex: "FEMALE"

The red dashed rectangle encloses the entire row 3, indicating missing data for this entry.

# The second image displays that row number 3 is removed if we drop all rows with missing data with df.dropna():


