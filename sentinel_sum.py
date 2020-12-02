sum = 0
i = 0
while True:
    i = int(input("Type a number: "))
    if i == -1:
        print("Sum is",sum)
        break
    sum += i
