size=int(input())
n=size
tsunami=[]
if size%2==0:
    for i in range(size):
        for j in range(size):
            if i+1>j: print("#",end="")
            else: print(".",end="")
        print()
        n-=1
else: 
    for i in range(size):
        for j in range(size):
            if j<n-1 : print(".",end="")
            else : print("#",end="")
        print()
        n-=1