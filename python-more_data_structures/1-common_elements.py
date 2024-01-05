def common_elements(set_1, set_2):
    # Initialize an empty set to store common elements
    common_set = set()

    # Iterate over elements in the first set
    for element in set_1:
        # Check if the element is also in the second set
        if element in set_2:
            # If yes, add it to the common_set
            common_set.add(element)

    return common_set

set_1 = {1, 2, 3, 4, 5}
set_2 = {4, 5, 6, 7, 8}

result = common_elements(set_1, set_2)
print(result)
