def fibonacci_sequence(n):
    """
    Generates a list of the first n Fibonacci numbers.

    Parameters:
    n (int): The number of Fibonacci numbers to generate.

    Returns:
    list: A list of the first n Fibonacci numbers.
    """
    if n <= 0:
        return [] 

    fibonacci_numbers = [0, 1]
    while len(fibonacci_numbers) < n:
        next_number = fibonacci_numbers[-1] + fibonacci_numbers[-2]
        fibonacci_numbers.append(next_number)

    return fibonacci_numbers[:n]

# EXAMPLE:
num_terms = 8
fibonacci_result = fibonacci_sequence(num_terms)
print(f"The first {num_terms} Fibonacci numbers are: {fibonacci_result}")