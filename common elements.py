# Take two lists, say for example these two:
#
#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#   b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that are common between the lists (without duplicates).
# Make sure your program works on two lists of different sizes.
#
# Extras:
#
# Randomly generate two lists to test this

from random import randint

list_1 = []
list_2 = []
common = []
for x in range(1, randint(1,50)):
    list_1.append(randint(1, 100))

for x in range(1, randint(1,50)):
    list_2.append(randint(1, 100))

for y in list_1:
    if y in list_2:
        common.append(y)

print(list_1, list_2)

print('Common elements are:')

print(common)