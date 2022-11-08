import logging

# Homework "debug"
logging.basicConfig(filename='sample.log', level=logging.INFO)  # Creating a file sample.log to record logs.


# Setting the log level info


def debug(func):  # Decorator function
    def wrapper(a, b):  # Additional function
        logging.info(f' {func.__name__}, value a: {a}, value b {b}')  # The log records the name of the function
        # and the value of the variables
        logging.info(f'{func(a, b)}')  # The log records result of the function
        print(func(a, b))  # Output of the function result to the console
        return func(a, b)  # Returns the result of the function

    return wrapper  # Returns a nested function


@debug  # Decorator function
def func_sum(a, b):  # Decorated function
    return a + b


func_sum(2, 3)  # Execution of the function

# Additional homework "new list"

list_ = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Source list


def decorator(funk):  # Decorator function
    def wrapper(list_i):  # Additional function
        list_1 = funk(list_i)  # Pass it to a variable decorated function and parameter
        return len([i[a] for i in list_ for a in range(3) if i[a] not in list_1])  # Return the number
        # of numbers not divisible by 3

    return wrapper  # Returns a nested function


@decorator
def new_list(list_i: list):  # Decorated function return list
    list_3 = [i[a] for i in list_i for a in range(3) if i[a] % 3 == 0]  # Generating a list
    # of numbers that are multiples of 3
    return list_3  # Return list


print(new_list(list_))  # Execution of the function
