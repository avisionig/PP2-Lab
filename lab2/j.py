def num(str):
    cnt=0
    for i in range (len(str)):
        if "0"<=str[i]<="9":
            cnt+=1
    if cnt>=1:
        return True
size=int(input())
list=[]
for i in range (size):
    str=input()
    if str not in list and str!=str.lower() and str!=str.upper() and num(str)==True:
        list.append(str)
list.sort()
print(len(list))
for i in list:
    print(i)
