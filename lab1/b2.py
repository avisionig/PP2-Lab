def tastyness(dish,i):
    if i<1:
        return 0
    else:
        return ord(dish[i-1])+tastyness(dish,i-1)
dish=input()
l=len(dish)
if tastyness(dish,l)>300:
    print("It is tasty!")
else:
    print("Oh, no!")
