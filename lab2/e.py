numbers=input().split()
if len(numbers)==1:
    size=int(numbers[0])
    x=int(input())
else:
    size=int(numbers[0])
    x=int(numbers[1])
xor=x
for i in range(1,size):
    xor=xor^(x+2*i)
print(xor)
