import randint from random

print("!!!   ROCK    PAPER    SCISSORS   !!!")
x = 0
result = [0, 0]
while x < 3:
    comp = randint(1, 3)
    print(" 1 - rock "
          " 2 - paper"
          " 3 - scissors")
    choice = int(input("rock, paper or scissors? "))

    # checking winner
    while choice in range(1, 4):
        print(f"\nI chose {comp}\n")
        if choice == comp:
            print("It's a tie!")
        elif choice == 1:
            if comp == 3:
                print("You win!")
                result[0] += 1
                x += 1
            elif comp == 2:
                print("You've lost!")
                result[1] += 1
                x += 1
        elif choice == 2:
            if comp == 1:
                print("You win!")
                result[0] += 1
                x += 1
            elif comp == 3:
                print("You've lost!")
                result[1] += 1
                x += 1
        elif choice == 3:
            if comp == 2:
                print("You win!")
                result[0] += 1
                x += 1
            elif comp == 1:
                print("You've lost!")
                result[1] += 1
                x += 1
        break
    else:
        print("You need to choose from 1, 2 and 3")

    print(f"\nActual result is {result}")

else:
    if result[0] > result[1]:
        print("!!!    YOU    WON    !!!")
    else:
        print("Sadly, You didn't win")
