def loop_mystery_exam5(x, y):
    z = y
    while x % z == 0:
        print("(" + str(x) + " " + str(z) + ") ", end='')
        x = x - z
        z += 1
    print("(" + str(x) + " " + str(z) + ") " + str(y))


loop_mystery_exam5(27, 3)