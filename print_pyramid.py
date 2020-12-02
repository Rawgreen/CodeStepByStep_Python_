
def print_pyramid():

    for i in range (1,7):
        print(" ",end='')
        if i == 6:
            print("*")
    
    for i in range(1,6):
        print(" ", end='')
        if i == 5:
            print("*"*3)

    for i in range(1,5):
        print(" ", end='')
        if i == 4:
            print("*"*5)
    
    for i in range(1,4):
        print(" ", end='')
        if i == 3:
            print("*"*7)
    
    for i in range(1,3):
        print(" ", end='')
        if i == 2:
            print("*"*9)

    for i in range(1,2):
        print(" ", end='')
        if i == 1:
            print("*"*11)



print_pyramid()