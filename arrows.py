def A():
    print(" /\\")
    print("/  \\")

def refA():
    print("\\  /")
    print(" \\/")

def Y():
    print(" ||")
    print(" ||")
    A()

def X():
    refA()
    A()

def main():
    A()
    print()
    A()
    print()
    Y()
    print()
    X()
    print()

main()



