list=[]
n=int(input())
while n!=0:
    list.append(n)
    n=int(input())
for i in range ((len(list)//2)):
    print(list[i]+list[len(list)-i-1],end=" ")
if len(list)%2==1:
    print(list[len(list)//2])