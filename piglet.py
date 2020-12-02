import random

print("Welcome to Piglet!")
sum = 0
x = random.randint(1,6)
print("You rolled a", x)
sum += x
while True:
    inp = input("Roll again? ")
    if inp == 'y' or inp == "yes":
        roll = random.randint(1,6)
        sum += roll
        print("You rolled a", roll)
        if roll == 1:
            print("You got 0 points.")
            break
    
    elif inp == 'n' or inp == "no":
        print("You got", sum, "points.")
        break
