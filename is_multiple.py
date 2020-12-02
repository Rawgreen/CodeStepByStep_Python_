

def is_multiple(value1, value2):

    if value1 % value2 == 0:
        return True
    elif value2 % value1 == 0:
        return True
    elif value1 % value2 <= 1:
        return False
    else:
        return False