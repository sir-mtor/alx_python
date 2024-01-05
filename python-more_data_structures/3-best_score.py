def best_score(a_dictionary):
    # Check if the dictionary is not empty
    if a_dictionary:
        # Find the key with the maximum integer value
        best_key = max(a_dictionary, key=a_dictionary.get)
        return best_key
    else:
        # Return None if the dictionary is empty
        return None


student_scores = {'Alice': 90, 'Bob': 75, 'Charlie': 85, 'David': 95}

best_student = best_score(student_scores)
print(best_student)
