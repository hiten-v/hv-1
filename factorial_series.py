n=int(input("Enter value of n"))
s=0
fact=1
for a in range(1, n+1):
    fact=fact*a
    s=s+fact
print("The sum of series is",s)
