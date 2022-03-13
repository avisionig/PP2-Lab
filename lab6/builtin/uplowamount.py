str=input()
up,low=0,0
for i in str:
    if i>="A" and i<="Z": 
    #or if ord(i)>=65 and ord(i)<=90:
        up+=1
    elif i>="a" and i<="z":
    #or elif ord(i)>=97 and ord(i)<=122:
        low+=1
print ("Upper case letters:",up,"\n""Lower case letters:",low)
