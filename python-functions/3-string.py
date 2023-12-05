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

# Example usage:
temperature_fahrenheit = 98.6
temperature_celsius = convert_to_celsius(temperature_fahrenheit)
print(f"{temperature_fahrenheit} Fahrenheit is equal to {temperature_celsius:.2f} Celsius.")
