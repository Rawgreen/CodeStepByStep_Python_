def second_half_letters(txt):
    count = 0
    for i in range(0, len(txt)):            #     how long will the loop turn     
        
        char = ord(txt[i])                  # to turn characters into ASCII values  

        if 110 <= char <= 122 or 78 <= char <= 90:       # condition to determine alphabet interval
            count += 1

    return count

second_half_letters("ruminates")