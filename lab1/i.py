amount=int(input())
correct="@gmail.com"
a=[]
for i in range (amount):
    email=input()
    if correct in email:
        email=email.replace(correct,"")
        a.append(email)
    amount=amount-1
for i in a:
    print(i)
