'''
def raise_exception_msg(message=""):
    try:
        # Raise a name exception with the specified message
        raise NameError(message)
    except NameError as e:
        print("Name error occurred:", e)
    else:
        print("No exception occurred.")
    finally:
        print("Finally block executed.")

# Example usage:
custom_message = "This is a custom message."
raise_exception_msg(custom_message)
'''
def raise_exception_msg(message=""):
    raise NameError(message)

# Test the function
if __name__ == "__main__":
    try:
        raise_exception_msg("C is fun")
    except NameError as ne:
        print(ne)

