def permutation(s,x=0):
    if x==len(s):
        print("".join(s))
    for i in range (x,len(s)):
        string=[j for j in s]
        string[x],string[i]=string[i],string[x]
        permutation(string,x+1)
print(permutation(input()))