def reverse_chunks(s, k):
    dummy = ''
    i = 0
    while i + k <= len(s):
        slice = s[i:i+k]        
        dummy  += slice[::-1]
        i += k

    l = len(s) % k
    if l != 0:
        dummy += s[-l:]

    return dummy