def down(n):
    for i in range(n):
        yield i
list=[]
for i in down(int(input())):
    list.append(i)
print (*list[::-1])