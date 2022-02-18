import random
def guess_game():
    print("Hello! What is your name?")
    name=input()
    cnt=0
    answer=random.randint(1,20)
    print("Well,",name,", I am thinking of a number between 1 and 20.\nTake a guess.")
    num=int(input())
    while num!=answer:
        if num<answer:
            print("\nYour guess is too low.\nTake a guess.")
            num=int(input())
            cnt+=1
        else:
            print("\nYour guess is too high.\nTake a guess.")
            num=int(input())
            cnt+=1
    print ("\nGood job, ",name,"! You guessed my number in ", cnt+1," guesses!")
    exit()
guess_game()