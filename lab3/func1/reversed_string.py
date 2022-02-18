def reverse(i):
    while i>=0:
        print(list[i],end=" ")
        return reverse(i-1)
str=input().split()
list=[]
for i in str:
    list.append(i)
reverse(len(list)-1)