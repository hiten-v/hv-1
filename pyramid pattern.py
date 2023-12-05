t=int(input("Enter the ending limit"))
for i in range(1,t+1):
    for j in range(1,t+1):
        print(end='   ')
    t=t-1
    for k in range(1,i+1):
            print('',"*",end='   ')
    print()
