def convert_to_celsius(fahrenheit):
    """
    Converts a temperature from Fahrenheit to Celsius.

    Parameters:
    fahrenheit (float): The temperature in Fahrenheit.

    Returns:
    float: The temperature in Celsius.
    """
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius
