def root_mean_squared_error(actual, calculated):
  if len(actual) != len(calculated):
    raise ValueError("Actual and calculated lists must have the same length.")

  errors = [(a - c)**2 for a, c in zip(actual, calculated)]
  return (sum(errors) / len(actual))**.5

# Example usage:
actual = [2, 3, 5, 5, 9]
calculated = [3, 3, 8, 7, 6]

rmse = root_mean_squared_error(actual, calculated)
print(f"Root Mean Squared Error: {rmse}")

from sklearn.metrics import mean_squared_error

def calculate_rmse(actual, calculated):
  """
  Calculates the Root Mean Squared Error (RMSE) between two lists.

  Args:
    actual: A list of actual values.
    calculated: A list of calculated values.

  Returns:
    The Root Mean Squared Error.
  """
  mse = mean_squared_error(actual, calculated)
  return mse ** 0.5

# Example usage:
actual = [2, 3, 5, 5, 9]
calculated = [3, 3, 8, 7, 6]

rmse = calculate_rmse(actual, calculated)
print(f"Root Mean Squared Error: {rmse}")