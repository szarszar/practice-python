from random import randint

liczba = "2345"


def index_collection(iterable):
    touples = []
    step = -1
    for x in iterable:
        touple = (x, step + 1)
        touples.append(touple)
        step += 1
    return touples


random_digits = ''
for x in range(1, 5):
    random_digits += str(randint(0, 9))
print(random_digits)

user_choice = input("Try to guess 4 digit number: ")

cows = 0
bulls = 0

user_index_list = index_collection(user_choice)
program_index_list = index_collection(random_digits)


for x in range(0, len(random_digits)):
    if user_index_list[x] == program_index_list[x]:
        cows += 1
    else:
        bulls += 1


print(f'You have {cows} cows and {bulls} bulls')
