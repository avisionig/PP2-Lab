message=input()
message=message.split(" ")
decihpered=""
for i in message:
    if len(i)>=3:
        decihpered+=i
        decihpered+=" "
print(decihpered)
    