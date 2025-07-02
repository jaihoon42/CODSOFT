
# Password Generator 


import random
import string

def generate_password(length):
    # Combine all character sets
    characters = string.ascii_letters + string.digits + string.punctuation
    # Randomly select characters from the set
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

print("Welcome to the Password Generator!")
try:
    length = int(input("Enter the desired password length: "))
    if length <= 0:
        print("Please enter a positive number.")
    else:
        password = generate_password(length)
        print("Generated Password:", password)
except ValueError:
    print("Invalid input. Please enter a numeric value.")