def multiple_returns(sentence):
    if len(sentence) == 0:
        return (0, None)
    else:
        return (len(sentence), sentence[0])

# Example usage:
result = multiple_returns("Hello, world!")
print(result)  # Output: (13, 'H')

empty_result = multiple_returns("")
print(empty_result)  # Output: (0, None)
