import secrets
import random
import string


def generate(total, numbers, lower, upper, spec, amount, output):
    passwords = []
    for _ in range(amount):
        if total:
            passwords.append(''.join(
                [secrets.choice(string.digits + string.ascii_letters + string.punctuation) for _ in range(total)]
            ))
        else:
            password = []
            for _ in range(numbers):
                password.append(secrets.choice(string.digits))
            for _ in range(upper):
                password.append(secrets.choice(string.ascii_uppercase))
            for _ in range(lower):
                password.append(secrets.choice(string.ascii_lowercase))
            for _ in range(spec):
                password.append(secrets.choice(string.punctuation))
            random.shuffle(password)
            password = "".join(password)
            passwords.append(password)
    if output:
        with open(output, 'w') as f:
            f.write('\n'.join(passwords))
    print('\n'.join(passwords))