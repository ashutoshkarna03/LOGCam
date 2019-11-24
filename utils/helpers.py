import random
import string


def generate_random_string(string_length=32):
    """Generate a random string of letters and digits """
    random_string = string.ascii_letters + string.digits
    return ''.join(random.choice(random_string) for i in range(string_length))






