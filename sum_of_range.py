
def sum_of_range(a, b):
    sumnum = 0
    if a >= b:
        print("0")
    
    for number in range(a,b+1):                     
        sumnum = number + sumnum
        #print(sumnum)
    return sumnum
    
        
sum_of_range(3, 7)
