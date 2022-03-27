def a_b_square(a,b):
    for i in range(a,b):
        yield i*i
for i in a_b_square(int(input()),int(input())):
    print (i)
""""import math
def a_b_square(a,b):
    for i in range(a,b):
        if i**(0.5)==int(i**(0.5)):
            yield i
for i in a_b_square(int(input()),int(input())):
    print (i)
"""