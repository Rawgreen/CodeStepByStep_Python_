def main():
    x = "happy"
    y = "pumpkin"
    z = "orange"
    pumpkin = "sleepy"
    happy = "vampire"

    orange(y, x, z)
    orange(x, z, y)
    orange(pumpkin, z, "y")
    z = "green"
    orange("x", "pumpkin", z)
    orange(y, z, happy)

def orange(z, y, x):
    print(y + " and " + z + " were " + x)

main()