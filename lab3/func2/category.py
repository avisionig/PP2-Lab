import list
movies_imported=list.movies
genre=input()
def category():
    list=[]
    for i in movies_imported:
        if i["category"]==genre:
            list.append(i["name"])
    return list
print(category())
