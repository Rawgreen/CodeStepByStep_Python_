def print_range(start_letter, end_letter):
    for i in range(ord(end_letter) - ord(start_letter) + 1):
        letter = chr(ord(start_letter) + i)
        print(letter, end='')

    print()


print_range("z", "a")
