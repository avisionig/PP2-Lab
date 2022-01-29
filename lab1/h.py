str=input()
letter=input()
cnt=[]
j=0
m=0
for i in str:
    if i==letter:
        cnt.append(j)
    j=j+1
l=len(cnt)
if l>1:
    a=cnt[0];b=cnt[l-1]
    print("{0}" " " "{1}".format(a,b))
else:
    print(cnt[0])

