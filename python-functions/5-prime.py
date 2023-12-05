def is_prime(number):
    """
    Checks if a given number is prime.

    Parameters:
    number (int): The input number.

    Returns:
    bool: True if the number is prime, False otherwise.
    """
    if number < 2:
        return False  
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False  
    return True  # No divisors found, the number is prime
