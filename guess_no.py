import random
n=random.randint(1,15)
c=0
while c<5:
    g=int(input("Enter"))
    if g==n:
        print("YOU WIN")
        break
    else:
        print("WRONG CHOICE")
        c+=1
else:
    print("YOU LOOSE")
    print(n)
