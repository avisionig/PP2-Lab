s=input()
condition=False
distance=''
cartriges=''
s=s.split(" ")
distance=s[0];distance=int(distance)
cartriges=s[1];cartriges=int(cartriges)
if distance>500:
    print("Try next time!")
    exit()
if distance>1:
    for i in range(2,distance):
        if distance%i==0:
            condition=True
            break
if condition==False and cartriges%2==0:
    print("Good job!")
else:
    print("Try next time!")

