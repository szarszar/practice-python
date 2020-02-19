# Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password every time the user asks for a new password. Include your run-time code in a main method.

# Extra:

# Ask the user how strong they want their password to be
import string
from random import randint


password = ''
while True:
    print("type done when finished")
    symbols_count = input("How many characters You want in Your password?: ")
    if symbols_count == 'done':
        break
    else:

     # 1- digit ; 2- small letter ; 3- capital letter ; 4- special symbol

        for x in range(1, int(symbols_count) + 1):
            kind = randint(1, 5)
            if kind == 1:
                password += str(randint(0, 10))
            elif kind == 2:
                password += string.ascii_lowercase[randint(
                    1, len(string.ascii_lowercase))]
            elif kind == 3:
                password += string.ascii_uppercase[randint(
                    1, len(string.ascii_uppercase))]
            elif kind == 4:
                password += string.punctuation[randint(
                    1, len(string.punctuation))]

        print(f"Your password: " + password)
