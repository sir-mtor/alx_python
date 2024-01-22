''''
def raise_exception():
    try:
        # Raise a type exception by attempting to convert a string to an integer
        value = int("abc")
    except TypeError as e:
        print("Type error occurred:", e)
    else:
        print("No exception occurred.")
    finally:
        print("Finally block executed.")

# Example usage:
raise_exception()
'''
def raise_exception():
    raise TypeError("Exception raised")

# Test the function
if __name__ == "__main__":
    try:
        raise_exception()
    except TypeError as te:
        print("Exception raised")
