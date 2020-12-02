
def print_powers_of_n(number, exponent):

    for i in range(0,exponent+1):
        normal = number
        normal **=i
        print(normal,end=' ')

print_powers_of_n(5,6)