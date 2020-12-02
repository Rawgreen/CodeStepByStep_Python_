def print_numbers2():
    for i in range (1,5):
        print(".", end='')
        if i == 4:
            print("1")
    
    for b in range(1,4):
        print(".", end="")
        if b == 3:
            print("2"*2)
    
    for c in range(1,3):
        print(".", end="")
        if c == 2:
            print("3" * 3)

    for d in range(1,2):
        print(".", end="")
        if d == 1:
            print("4" * 4)
    for e in range(1,6):
        print("5", end="")


print_numbers2()