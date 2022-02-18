import list
movies_imported=list.movies
genre=input()
def aver():
    sum=0
    cnt=0
    for i in movies_imported:
        if i["category"]==genre:
            sum+=i["imdb"]
            cnt+=1
    sum=sum/cnt
    return sum
print(aver())