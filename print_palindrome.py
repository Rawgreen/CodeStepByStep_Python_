def print_palindrome():
    txt = input("Type one or more words: ")
    text = txt.lower()
    if text[0::] == text[::-1]:
        print(txt, "is a palindrome!")
    else:
        print(txt, "is not a palindrome.")

print_palindrome()

