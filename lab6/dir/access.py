import os
print ("Existence:", os.access('C:\\Users\\ayan\\Desktop\\folder\\vscode\\python\\lab6\\forprob\\hello world.txt', os.F_OK))
print ("Readability:", os.access('C:\\Users\\ayan\\Desktop\\folder\\vscode\\python\\lab6\\forprob\\hello world.txt', os.R_OK))
print ("Writability:", os.access('C:\\Users\\ayan\\Desktop\\folder\\vscode\\python\\lab6\\forprob\\hello world.txt', os.W_OK))
print ("Executability:", os.access('C:\\Users\\ayan\\Desktop\\folder\\vscode\\python\\lab6\\forprob\\hello world.txt', os.X_OK))