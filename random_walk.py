import random
def random_walk(value):
    pos = 0
    count = 0
    biggest = 0
    while pos != value or pos != -value:
        walk = random.randint(1,2)

        if walk == 1:       #straight                       
            count += 1
            pos += 1
            print("Position =", pos)
            if pos > biggest:
                biggest = pos


        if walk == 2:         #backward
            count +=1
            pos -=1
            if pos > biggest:
                biggest = pos
            print("Position =", pos)

        if pos == value or pos == -value:
            print("Finished after", count , "step(s)")
            print("Max position =", biggest)
            break

random_walk(3)