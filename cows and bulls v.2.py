from random import randint


def index_collection(iterable):
    tuples = []
    step = -1
    for x in iterable:
        pair = (x, step + 1)
        tuples.append(pair)
        step += 1
    return tuples


random_digits = ''
for x in range(1, 5):
    random_digits += str(randint(0, 9))
print(random_digits)

program_index_list = index_collection(random_digits)


while True:
    cows = 0
    bulls = 0
    user_choice = input("Try to guess 4 digit number: ")
    user_index_list = index_collection(user_choice)
    for x in range(0, len(random_digits)):
        touple = user_index_list[x]
        if user_index_list[x] == program_index_list[x]:
            cows += 1
        elif touple[0] in random_digits:
            bulls += 1
    if cows == 4:
        print("Well done! Yo've guessed all the digits!")
        break
    else:
        print(f'You have {cows} cows and {bulls} bulls, try again')
