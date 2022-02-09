year=[]
while True:
    dates=input().split()
    if dates[0]=="0":
        break
    year.append((dates[2],dates[1],dates[0]))
year=sorted(year)
for i in year:
    print(i[2],i[1],i[0])