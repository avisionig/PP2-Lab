essay=input()
essay=essay.replace(",","").replace("!","").replace("?","").split()
word=[]
for i in essay:
    if i not in word:
        word.append(i)
word.sort()
print(len(word))
for i in word:
    print(i)