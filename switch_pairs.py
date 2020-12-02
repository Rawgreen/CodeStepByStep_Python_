


def switch_pairs(txt):
    
    dum = ''
    i = 0
    if len(txt) < 2:
        return txt

    while i < len(txt) -1:
        dum += txt[i + 1]
        dum += txt[i]
        i += 2

    if len(txt) % 2 != 0:
        dum += txt[-1]
    return dum
        
