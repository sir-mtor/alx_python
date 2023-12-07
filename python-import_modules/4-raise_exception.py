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
