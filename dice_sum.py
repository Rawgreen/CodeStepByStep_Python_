import random

def dice_sum():
    desire = int(input("Desired dice sum: "))
    sum = 0
    while True:
        roll1 = random.randint(1, 6)
        roll2 = random.randint(1, 6)
        sum = roll1 + roll2
        print(roll1, "and", roll2 , "=", sum)
        if sum == desire:
            break

dice_sum()