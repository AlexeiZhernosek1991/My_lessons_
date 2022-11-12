list_ = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Source list


def decorator(funk):  # Decorator function
    quantity = 9

    def wrapper(list_i):  # Additional function
        list_1 = funk(list_i)  # Pass it to a variable decorated function and parameter
        len_list_1 = len(list_1)
        nonlocal quantity
        quantity = len([i[a] for i in list_ for a in range(3)]) - len_list_1
        return quantity
    return wrapper  # Returns a nested function


@decorator
def new_list(list_i: list):  # Decorated function return list
    list_3 = [i[a] for i in list_i for a in range(3) if i[a] % 3 == 0]  # Generating a list
    # of numbers that are multiples of 3
    return list_3  # Return list


print(new_list(list_))  # Execution of the function
