def reverse_string(string):
    """
    Reverses a given string.

    Parameters:
    string (str): The input string.

    Returns:
    str: The reversed string.
    """
    reversed_str = string[::-1]
    return reversed_str

# Example usage:
input_str = "Hello, World!"
reversed_result = reverse_string(input_str)
print(f"The reverse of '{input_str}' is: '{reversed_result}'")

