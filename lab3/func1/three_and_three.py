def has_33(i,j):
    cnt=0
    while j<len(list):
        if list[i]==3 and list[j]==3:
            return True
            exit()
        return has_33(i+1,j+1)
    return False
nums=input().split()
list=[]
for i in nums:
    list.append(int(i))
print(has_33(0,1))