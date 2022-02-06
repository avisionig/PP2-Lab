size_demons=int(input())
demons={}
for i in range (size_demons):
    demon_name, weakness=input().split()
    if weakness not in demons:
        demons[weakness]=1
    else:
        demons[weakness]=demons[weakness]+1
size_hunters=int(input())
hunters={}
for i in range (size_hunters):
    hunter_name, element, num=input().split()
    if element not in hunters:
        hunters[element]=int(num)
    else:
        hunters[element]=hunters[element]+int(num)
cnt=0
for i in demons:
    if i in hunters:
        demons[i]=demons[i]-hunters[i]
    if demons[i]>0:
        cnt=cnt+demons[i]
print("Demons left:", cnt)