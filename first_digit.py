
def first_digit(a):
    number = a
    if number < 0:
        number = number * -1
    while(number >= 10):
        number = number // 10

    return number
        


