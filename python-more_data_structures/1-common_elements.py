def common_elements(set_1, set_2):
    # Use the intersection operation to find common elements between the two sets
    common_set = set_1 & set_2
    return common_set

'''
set_1 = {"Python", "C", "Javascript"}
set_2 = {"Bash", "C", "Ruby", "Perl"}
c_set = common_elements(set_1, set_2)
print(sorted(list(c_set)))
'''