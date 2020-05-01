# Given an integer, , perform the following conditional actions:
#
# If  is odd, print Weird
# If  is even and in the inclusive range of 2 to 6, print Not Weird
# If  is even and in the inclusive range of 6 to 20, print Weird
# If  is even and greater than , print Not Weird

number = int(input("Write a number from 1 to 100: "))
if number in range(1, 100):
    if number % 2 != 0:
        print("Weird")
    elif number in range(6, 20):
        print("Weird")
    else:
        print("Not wierd")
else:
    print("Wrong number")