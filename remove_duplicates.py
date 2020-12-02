def remove_duplicates(txt):

    s = set()
    list = []
    for ch in txt:
        if ch not in s:
            s.add(ch)
            list.append(ch)

    return ''.join(list)
