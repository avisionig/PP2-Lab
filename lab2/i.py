size=int(input())
cartoons=[]
taken=[]
for i in range(size):
    str=input().split()
    if str[0]=="1":
        cartoons.append(str[1])
    else:
        taken.append(cartoons[0])
        del cartoons[0]
print(*taken)

