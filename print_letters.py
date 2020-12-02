def print_letters(txt):
    let = len(txt)              # how long will the loop turn
    a = 0
    for i in range(0, let-1):
        if txt[a] == "":
            continue
        print(txt[a], end='-')
        a += 1

    if txt == "":           #for empty entry
        print("")
    else:
        print(txt[-1])      # fence post problem
print_letters("")