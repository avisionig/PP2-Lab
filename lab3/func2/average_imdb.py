import list
movies_imported=list.movies
def aver():
    sum=0
    cnt=0
    for i in movies_imported:
        sum+=i["imdb"]
        cnt+=1
    sum=sum/cnt
    return sum
print(aver())