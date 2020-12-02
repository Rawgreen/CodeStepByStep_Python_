
def even_sum():

    prompt = int(input("how many integers? "))

    sum = 0
    max = 0

    for i in range(prompt):
        
        sonraki = int(input("next integer? "))

        if sonraki % 2 == 0:

            sum += sonraki
            if(sonraki > max):
                max = sonraki
    
    print("even sum =", sum)
    print("even max =", max)