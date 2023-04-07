import random
import string


def generate_secret_key():
    """
    Generate a random SECRET_KEY for Django projects.

    This function creates a 50-character-long random string that can be used as
    a SECRET_KEY in Django projects. It includes a mix of ASCII characters,
    digits, and punctuation.

    Returns:
        str: A 50-character-long random string to be used as a SECRET_KEY.

    Usage:
        1. Run this script from the command line:
            python generate_secret_key.py

        2. The script will print a new SECRET_KEY to the console.

        3. Copy the generated SECRET_KEY and replace the existing SECRET_KEY
           value in your Django project's settings.py file.
    """
    chars = string.ascii_letters + string.digits + string.punctuation
    secret_key = ''.join(random.choice(chars) for _ in range(50))
    return secret_key


if __name__ == '__main__':
    print(generate_secret_key())
