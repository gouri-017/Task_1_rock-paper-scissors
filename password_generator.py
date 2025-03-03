import string
import random


def generate_password(length, numbers, symbols, characters):
    if length < numbers + symbols + characters:
        print("Length is too short for the given parameters.")
        return

    password = []

    # Add required numbers, symbols, and characters
    for i in range(numbers):
        password.append(str(random.randint(0, 9)))

    for i in range(symbols):
        password.append(random.choice(string.punctuation))

    for i in range(characters):
        password.append(random.choice(string.ascii_letters))

    # Fill the remaining length with random choices from all character types
    remaining_chars = length - (numbers + symbols + characters)
    for i in range(remaining_chars):
        password.append(random.choice(string.ascii_letters + string.digits + string.punctuation))

    random.shuffle(password)
    return ''.join(password)


# User inputs
length = int(input("Total password length? "))
numbers = int(input("How many numbers? "))
symbols = int(input("How many symbols? "))
characters = int(input("How many characters? "))

# Generate and print password
print(generate_password(length, numbers, symbols, characters))