import list
movies_imported=list.movies
def above_55():
    for i in movies_imported:
        if i["name"]==movie and i["imdb"]>5.5:
            return True
    return False
print(above_55())