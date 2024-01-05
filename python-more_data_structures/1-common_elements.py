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

set_1 = { "Python", "C", "Javascript" }
set_2 = { "Bash", "C", "Ruby", "Perl" }
c_set = common_elements(set_1, set_2)

result = common_elements(set_1, set_2)
print(result)
