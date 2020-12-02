def is_vowel(s):
    vowels = 'AEIOUaeiou'
    if len(s) != 1:
        return False
    if s in vowels:
        return True
    return False

def is_all_vowels(s):
    for ch in s:
        if ch.isalpha() and not is_vowel(ch):
            return False
    return True    