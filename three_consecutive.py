def three_consecutive(val, num, var):

    lis = [val, num, var]

    lis.sort()

    if lis[1] == lis[0] + 1 and lis[2] == lis[1] + 1:
        return True 
    return False