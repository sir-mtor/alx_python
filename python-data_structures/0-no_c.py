def no_c(my_string):
    result = ""
    for char in my_string:
        if char.lower() != 'c':
            result += char
    return result

# Example usage:
input_string = "This is a string with C and c characters."
output_string = no_c(input_string)
print(output_string)
