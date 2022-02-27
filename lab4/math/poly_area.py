import math 
sides,len=float(input("Input number of sides:")),float(input("Input the length of a side:"))
print("The area of the polygon is:", math.floor(((len**2)*sides)/(4*math.tan(math.pi/sides))))