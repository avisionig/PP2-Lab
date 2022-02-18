def new_list(i):
    while i<len(list):
        if list[i] not in set:
            set.append(list[i])
        i+=1
nums=input().split()
list=[]
set=[]
for i in nums:
    list.append(int(i))
new_list(0)
print(*set)
