
def random_rects():
    print("How many recangles? ",end='')
    rectangle = int(input())

    for values in range(1,rectangle+1):             #taking input for rectangle shapes
        
        print("Width ", values , "? ",end='')
        Width = int(input())

        print("Height", values, "? ",end='')
        Height = int(input())

        for area in range (1,rectangle+1):                #Calculating area     
            Area = Width * Height                                                       ##### NOT DONE #####
            print("Area ", area, "=" , Area)
            

        for shape in range(1,Height+1):                 #Printing rectangles
            print("*" * Width, end='')
            print("")


random_rects()

    