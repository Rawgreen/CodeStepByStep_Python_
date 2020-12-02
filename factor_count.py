
def factor_count(integer):
    count = 0

    for i in range(1,integer +1):

        if (integer % i == 0):
            count += 1
        

    return count

factor_count(24)
