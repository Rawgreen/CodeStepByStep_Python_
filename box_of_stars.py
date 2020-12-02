def box_of_stars(width,height):
    for x in range (width):
        print("*",end="")
    print("")
    for k in range (2,height):
        for y in range (width):
            if y==0:
                print("*",end="")
            if 0<y<width-1:
                print(" ",end="")
        
            if y==width-1:
                print("*")
    for t in range (width):
        print("*",end="")
        

box_of_stars( 8, 5)