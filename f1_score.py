# Function to calculate f1_score
def calc_f1_score(tp, fp, fn):
    # Check if the input values are of type int
    if not isinstance(tp, int) or not isinstance(fp, int) or not isinstance(fn, int):
        if not isinstance(tp, int):
            print('tp must be int')
        if not isinstance(fp, int):
            print('fp must be int')
        if not isinstance(fn, int):
            print('fn must be int')
        return  # Ensure the program stops

    # Check if the input values are all greater than 0
    if tp <= 0 or fp <= 0 or fn <= 0:
        print('tp, fp, and fn must be greater than zero')
        return

    # Calculate the values
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1_score = 2 * (precision * recall) / (precision + recall)

    # Print the calculated values
    print(f'precision is {precision}')
    print(f'recall is {recall}')
    print(f'f1_score is {f1_score}')


# Call the function with sample values
calc_f1_score(tp = 2, fp = 3, fn = 4)

calc_f1_score(tp = 'a', fp = 3 , fn = 4)

calc_f1_score(tp = 2, fp = 'a', fn = 4)

calc_f1_score(tp = 2, fp = 3, fn = 'a')

calc_f1_score(tp = 2, fp = 3, fn = 0)
