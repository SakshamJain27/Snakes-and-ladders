import dice
import Check

print("Welcome to snake and ladders")
print("Let's start")

pos = 0

while True:
    choice = input("Press r to roll the dice and q to quit")
    if choice == "q":
        print("Quiting the game")
        quit()

    else:
        rolled_num = dice.roll()
        pos = pos + rolled_num
        if Check.check(pos) == "snakes":
            print("Sorry, you will have to start from 10 again")
            pos = 10

        elif Check.check(pos) == "ladders":
            print("You were on", pos)
            print("You are moving up")
            pos = pos + 5
            print("Now you are on", pos)
            if pos>100:
                print("You won the game")
                quit()
        else:
            print("Now you are on", pos)
            if pos>100:
                print("You won the game")
                quit()


