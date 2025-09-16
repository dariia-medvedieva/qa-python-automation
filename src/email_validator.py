import re

def validate_email(email: str) -> bool:
    """
    Validates if the given email string is in a proper format.

    Args:
        email (str): The email address to validate.

    Returns:
        bool: True if the email is valid, False otherwise.
    """
    # Define a simple regex pattern for validating email addresses
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    # Use regex to check if the email matches the pattern
    if re.match(pattern, email):
        return True
    return False
