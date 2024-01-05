def update_dictionary(a_dictionary, key, value):
    # Update the value if the key already exists
    if key in a_dictionary:
        a_dictionary[key] = value
    else:
        # Add a new key-value pair if the key doesn't exist
        a_dictionary[key] = value
    
    return a_dictionary

# Example usage:
my_dictionary = {'a': 1, 'b': 2, 'c': 3}

update_dictionary(my_dictionary, 'b', 5)  # Replace value for existing key 'b'
update_dictionary(my_dictionary, 'd', 4)  # Add a new key-value pair 'd': 4

print(my_dictionary)
