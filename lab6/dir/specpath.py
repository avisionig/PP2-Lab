import os
path='C:\\Users\\ayan\\Desktop\\folder\\vscode\\python\\lab6\\forprob'
list=os.listdir(path)
dirlist=[]
filelist=[]
for name in list:
    if os.path.isdir(os.path.join(path,name)):
        dirlist.append(name)
    elif os.path.isfile(os.path.join(path,name)) :
        filelist.append(name)
print("Directories",dirlist,"\n""Files",filelist, "\n""All", list)
