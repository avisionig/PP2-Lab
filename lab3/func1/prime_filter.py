def filter(a):
    for i in range (2,a):
        if a%(i)==0:
            return True
    return False
numbers=input().split()
primes=[]
for i in range (len(numbers)):
    if filter((int(numbers[i])))==False and int(numbers[i])!=1:
        primes.append(numbers[i])
print(*primes)

