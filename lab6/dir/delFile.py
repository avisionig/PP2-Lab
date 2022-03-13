import os
path='C:\\Users\\ayan\\Desktop\\folder\\vscode\\python\\lab6\\dir\\del_file.txt'
if os.access(path,os.F_OK):
    os.remove('del_file.txt')
    print('File deleted')
else:
    print('File do not exits')
    a=open('del_file.txt', 'x')