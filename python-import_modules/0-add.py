# File: add_0.py
# def add(a, b):
#    return a + b

# Main program
a = 1
b = 2

# Do not use * for importing or __import__
add_module = __import__('add_0')

# Use variables a and b as arguments when calling the function
result = add_module.add(a, b)

# Display the result using print function with string format
print("{} + {} = {}".format(a, b, result))

