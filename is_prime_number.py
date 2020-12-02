def is_prime_number(value):
    if value > 1:
        for i in range(2,value):
            if value % i == 0:
                return False
        return True
    elif value < 0:
        for i in range(value,-2):
            if value % i == 0:
                return False
        return True
    elif value == 0 or value == 1:
        return False