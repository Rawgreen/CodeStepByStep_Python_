print("This program lists the Fibonacci sequence.")
maxval = int(input("Max value? "))

a, b = 0, 1
print("0, ", end='')
if maxval == 0 or maxval == 1:
        print("1, 1")
else:
    while b <= maxval:
        a, b = b, a+b
        if a + b == maxval:
            print(str(a) + ", " + str(b)+ ", "+ str(maxval))
            break
        if b >= maxval:
            print(a)
            break
        print(a, end=', ')
    


