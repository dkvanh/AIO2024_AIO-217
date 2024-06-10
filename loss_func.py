import random
import math

# Function to calculate Mean Absolute Error (MAE)
def calculate_mae(y_true, y_pred):
    return sum(abs(y_t - y_p) for y_t, y_p in zip(y_true, y_pred)) / len(y_true)

# Function to calculate Mean Squared Error (MSE)
def calculate_mse(y_true, y_pred):
    return sum((y_t - y_p) ** 2 for y_t, y_p in zip(y_true, y_pred)) / len(y_true)

# Function to calculate Root Mean Squared Error (RMSE)
def calculate_rmse(y_true, y_pred):
    mse = calculate_mse(y_true, y_pred)
    return math.sqrt(mse)

# Function to select regression loss function
def select_loss_function(num_samples, loss_name):
    # Check if num_samples is a valid integer
    if not num_samples.isnumeric():
        print('number of samples must be an integer number')
        return

    num_samples = int(num_samples)

    # Loop through num_samples to generate predictions and targets
    for i in range(num_samples):
        predict = random.uniform(0, 10)
        target = random.uniform(0, 10)

        # Calculate loss based on loss_name
        if loss_name == 'MAE':
            loss = calculate_mae([target], [predict])
        elif loss_name == 'MSE':
            loss = calculate_mse([target], [predict])
        elif loss_name == 'RMSE':
            loss = calculate_rmse([target], [predict])

        # Print the result
        print(f'{loss_name}, sample-{i}, predict: {predict}, target: {target}, loss: {loss}')

# Example usage
num_samples = input("Enter the number of samples: ")
loss_name = input("Enter the loss function name (MAE, MSE, RMSE): ")

select_loss_function(num_samples, loss_name)
