def hysto(i):
    if i==len(list):
        exit()
    else:
        print ('*'*(list[i]))
        return hysto(i+1)
nums=input().split()
list=[]
for i in nums:
    list.append(int(i))
hysto(0)