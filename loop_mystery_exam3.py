def loop_mystery_exam3(x, y):
    z = x+y
    while x > 0 and y > 0:
        x = x - y
        y -= 1
        print(str(x)+ " " + str(y) + " ", end='')
    print(str(y))
    print(z)

loop_mystery_exam3(7,5)