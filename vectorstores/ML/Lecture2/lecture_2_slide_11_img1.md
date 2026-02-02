# Here is what the image 1 in slide 11 of lecture 2 contains:

```
The image is a text-based output from a DataFrame in pandas, indicated by calling `df.info()`. It is formatted as follows:

- Title in red at the top: `df.info()`

- Metadata about the DataFrame is presented next:
  - `<class 'pandas.core.frame.DataFrame'>`
  - `RangeIndex: 344 entries, 0 to 343`
  - `Data columns (total 8 columns):`

- The DataFrame contains the following columns, listed in a table format with headings:
  - Column headers: `#`, `Column`, `Non-Null Count`, `Dtype`

- Each column is listed with accompanying information:
  - `0  species            344 non-null  object`
  - `1  island             344 non-null  object`
  - `2  bill_length_mm     342 non-null  float64`
  - `3  bill_depth_mm      342 non-null  float64`
  - `4  flipper_length_mm  342 non-null  float64`
  - `5  body_mass_g        342 non-null  float64`
  - `6  sex                334 non-null  object`
  - `7  year               344 non-null  int64`

- Following the column information, there is a small summary with:
  - `dtypes: float64(4), int64(1), object(3)`
  - `memory usage: 21.6+ KB`
```