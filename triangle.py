
def triangle(size):
    number = size - 1
    value = 1
    for i in range(size +1 , 1, -1):
        print(" "* number, end='')
        print("*" * value)
        number -= 1
        value +=1

triangle(5)