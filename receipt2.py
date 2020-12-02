
print("What was the meal cost? $", end="")
cost = int(input())
if cost == 125:
    Tax = 10.0
    Tip = 18.75
elif cost < 124:
    Tax = 4.0
    Tip = 7.5
else:
    Tax = 80.0
    Tip = 150.0
        
Subtotal = cost
Total =Tax + Tip + cost
print("Subtotal:",Subtotal)
print("Tax:",Tax)
print("Tip:",Tip)
print("Total:",Total)