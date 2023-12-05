def validate_password(password):
    """
    Validates a given password based on specific criteria.

    Parameters:
    password (str): The input password.

    Returns:
    bool: True if the password passes all the checks, False otherwise.
    """
    # Check length
    if len(password) < 8:
        return False

    # Check for at least one uppercase letter, one lowercase letter, and one digit
    has_uppercase = False
    has_lowercase = False
    has_digit = False

    for char in password:
        if char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
        elif char.isdigit():
            has_digit = True

    if not (has_uppercase and has_lowercase and has_digit):
        return False

    # Check for spaces
    if ' ' in password:
        return False

    return True  # Password passed all checks
