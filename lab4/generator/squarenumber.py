def gen(n):
    for i in range (n):
            yield i*i
for i in gen(int(input())):
        print (i)
