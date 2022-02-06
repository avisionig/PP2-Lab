size=int(input())
list=[[0] * size for i in range(size)]
for i in range(size):
    for j in range(size):
        if i==j:
            list[i][j]=i*i
        elif i==0:
            list[i][j]=j
        elif j==0:
            list[i][j]=i
for i in list:
    print(*i)
