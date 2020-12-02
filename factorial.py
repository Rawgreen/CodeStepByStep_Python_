def factorial(n):
    Factorial = 1
    if n == 0 or n == 1:                # Precaution in case 0 and 1 factorial are entered
        print(n ,"factorial =", "1")
    
    else:                               # the numbers that entered except 0 and 1 
        for i in range(1, n + 1):
            Factorial = Factorial * i   # sum of the numbers that have been multiplied

        print(n ,"factorial =", Factorial)

factorial(0)