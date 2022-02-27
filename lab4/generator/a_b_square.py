def a_b_square(a,b):
    for i in range(a,b):
        yield i*i
for i in a_b_square(int(input()),int(input())):
    print (i)