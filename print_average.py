def print_average():
    inp = 0
    sum = 0
    count = 0
    while True:
        inp = int(input("Type a number: "))
        if inp < 0 and count == 0:
            break
        if inp < 0:
            print("Average was", sum/count)
            break
        sum += inp
        count += 1

print_average()
