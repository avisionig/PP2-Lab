size=int(input())
numbers=input().split()
list=[]
for i in range (len(numbers)):
    if numbers[i]!=" ":
        list.append(int(numbers[i]))
max=0
for i in range (size):
    j=i+1
    if j==i:
        print(max)
        exit()
    while j!=size:
        if max<list[i]*list[j]:
            max=list[i]*list[j]
        j+=1
print(max)



