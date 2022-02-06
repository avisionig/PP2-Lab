size=int(input())
dict={}
max_val=0
for i in range (size):
    str = input().split()
    if str[0] not in dict:
        dict[str[0]]=int(str[1])
        if max_val<dict[str[0]]:
            max_val=int(str[1])
    else:
        dict[str[0]]=dict[str[0]]+int(str[1])
        if max_val<dict[str[0]]:
            max_val=dict[str[0]]
sorted_dict=sorted(dict.keys())
for name in sorted_dict:
    if max_val-dict[name]==0:
        print(name, "is lucky!")
    else:
        print(name, "has to receive", max_val-dict[name], "tenge")