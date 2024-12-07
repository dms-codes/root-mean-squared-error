# Root Mean Squared Error (RMSE) Calculation

This file demonstrates two ways to calculate the Root Mean Squared Error (RMSE) between two lists of values:

1. **Manual Calculation:** 
   - The `root_mean_squared_error` function calculates the RMSE directly by:
     - Checking for equal lengths of input lists.
     - Calculating the squared difference between corresponding values.
     - Summing the squared errors.
     - Calculating the mean of the squared errors.
     - Taking the square root of the mean squared error.

2. **Using scikit-learn:**
   - The `calculate_rmse` function leverages the `mean_squared_error` function from the scikit-learn library for efficient and concise RMSE calculation. 
     - It calculates the Mean Squared Error (MSE) using the scikit-learn function.
     - Then, it computes the square root of the MSE to obtain the RMSE.

## Example Usage

Both functions can be used as follows:

```python
actual = [2, 3, 5, 5, 9]
calculated = [3, 3, 8, 7, 6]

# Manual Calculation
rmse_manual = root_mean_squared_error(actual, calculated) 
print(f"Root Mean Squared Error (Manual): {rmse_manual}")

# Using scikit-learn
rmse_sklearn = calculate_rmse(actual, calculated)
print(f"Root Mean Squared Error (scikit-learn): {rmse_sklearn}")
