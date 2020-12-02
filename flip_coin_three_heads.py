import random


def flip_coin_three_heads():
    heads = 0
    tails = 0
    
    while heads != 3:

        chance = random.randint(0, 1)


        if chance == 1: 
            print("T", end=' ')                # tails == 1
            tails += 1
            heads = 0

        if chance == 0:
            print("H", end=' ')
            heads += 1
            
        if heads == 3:
            print()
            print("Three heads in a row!")
            break
            
    


flip_coin_three_heads()