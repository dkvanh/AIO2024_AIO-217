import math

# Function to check if a value is a number
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

# Activation functions
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def relu(x):
    return max(0, x)

def elu(x, alpha = 0.01):
    return x if x >= 0 else alpha * (math.exp(x) - 1)

# Main function to process the input
def main():
    x = input("Enter the value of x: ")
    act_func_name = input("Enter the activation function (sigmoid, relu, elu): ")

    # Check if x is a valid number
    if not is_number(x):
        print('x must be a number')
        return

    # Convert x to float
    x = float(x)

    # Dictionary of supported activation functions
    act_func = {
        'sigmoid': sigmoid,
        'relu': relu,
        'elu': elu
    }

    # Check if the activation function name is valid
    if act_func_name not in act_func:
        print(f'{act_func_name} is not supported')
        return

    # Calculate the result using the appropriate activation function
    if act_func_name == 'elu':
        result = act_func[act_func_name](x, alpha = 0.01)
    else:
        result = act_func[act_func_name](x)

    # Print the result
    print(f'{act_func_name}: f({x}) = {result}')

# Run the main function
if __name__ == "__main__":
    main()
