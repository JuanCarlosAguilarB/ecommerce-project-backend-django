import random
import string


def generate_verification_code(length=4):
    """
    Generate a verification code of specified length.

    :param int length: Length of the verification code (default is 4).
    :return: Verification code as a string.
    """
    if length <= 0:
        raise ValueError("Length should be a positive integer.")

    code = ''.join(random.choices(string.digits, k=length))
    return code
