def gen(n):
    for i in range (n):
            if i%2==0:
                yield i
for i in gen(int(input())):
        print (i,end=",")