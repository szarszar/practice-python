# Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)


word = input("word to check: ")

reverse = word[::-1]


if word == reverse:
    print(f'{word} is a palindrome')
else:
    print(f'{word} is not a palindrome')