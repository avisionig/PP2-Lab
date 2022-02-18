def palin(i,j):
    if i==len(str) or j<0:
        return True
    else:
        if str[i]==str[j]:
            return palin(i+1,j-1)
        else:
            return False
str=input()
print (palin(0,(len(str)-1)))   