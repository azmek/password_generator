import random
import string
import collections


def generate_random_password(total):
    password = create_random_string(total)

    while is_repeating(password, total):
        password = create_random_string(total)

    return "".join(password)


def create_random_string(
    total, chars=string.ascii_letters + string.digits + string.punctuation
):

    random_string = ''.join(random.choice(chars) for i in range(total))
    return random_string


def is_repeating(password, total):
    """ Check if there is any 2 characters repeating consecutively."""
    for i in range(total):
        random_string = random.sample(password, total)


if __name__ == "__main__":
    print(generate_random_password(random.randint(6, 30)))
