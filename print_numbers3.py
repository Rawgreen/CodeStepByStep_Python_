
def print_numbers3():

    for i in range(1,5):
        print(".", end='')
        if i == 4:
            print("1")
    
    for i in range(1,5):
        print(".", end='')
        if i == 3:
            print("2", end='')
    print("")

    for i in range(1,5):
        print(".", end="")
        if i == 2:
            print("3", end='')
    print("")

    for i in range(1,5):
        print(".", end="")
        if i == 1:
            print("4", end='')
    print("")

    for i in range(1,2):
        number = "5"
        print(number, end='')
        if i == 1:
            number = "."
            print(number * 4,end='')
            

print_numbers3()