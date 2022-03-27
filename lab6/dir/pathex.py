import os
path='C:\\Users\\ayan\\Desktop\\folder\\vscode\\python\\lab6\\forprob'
if os.path.exists(path):
    print("Exits\nFile name:",os.path.basename(path))
    print("Dir and files in path: ", os.listdir(path))
else: print("NO")
