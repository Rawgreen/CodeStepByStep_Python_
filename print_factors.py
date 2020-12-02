def print_factors(factor):
    for i in range(1, factor):
        if factor % i == 0:
            print(i,end =' and ')

    print(factor)

print_factors(1)


