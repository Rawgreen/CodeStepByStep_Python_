def digit_sum(n):
    s = 0
    if n < 0:
        n *= -1
    while n:
        s += n % 10
        n //= 10

    return s