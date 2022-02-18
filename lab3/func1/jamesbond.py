def spy_game():
    cnt_zero=0
    cnt_sev=0
    for i in list:
        if i==0:
            cnt_zero+=1
        if i==7 and cnt_zero>=2:
            return True
    return False
nums=input().split()
list=[]
for i in nums:
    list.append(int(i))
print(spy_game())
