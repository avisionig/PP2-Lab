brackets=input()
opened_brackets=["[","{","("]
closed_brackets=["]","}",")"]
list=[]
if len(brackets)%2!=0 :
    print("No")
    exit()
else:
    for i in brackets:
        if i in opened_brackets:
            list.append(i)
        elif i in closed_brackets:
            temp=closed_brackets.index(i)
            if((len(list)>0) and (opened_brackets[temp]==list[len(list)-1])):
                list.pop()
            else:
                print("No")
                exit()
    if len(list)==0:
        print("Yes")
    else:
        print("No")

