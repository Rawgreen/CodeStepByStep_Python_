
def count_even_digits(value, digits):
    count = 0
    while value > 0:
        number = value % 10
        if (number % 2 == 0):
            count +=1 
        value = int(value / 10)
    
    return count
    