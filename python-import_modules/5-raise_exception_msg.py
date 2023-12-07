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
