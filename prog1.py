''' Q. Given the names and grades for each student in a class of
students, store them in a nested list and print the name(s)
of any student(s) having the second lowest grade.
Note: If there are multiple students with the second lowest grade,
order their names alphabetically and print each name on a new line.'''

l2=[]
l=[]
f=[]
for i in range(int(input())):
    name = input()
    score = float(input())
    l.append([name,score])
for i in l:
    l2.append(i[1])
    l2.sort()
t=l2[0]
for i in l2:
    if i>t:
        t=i
        break
for i in l:
    if i[1]==t:
        f.append(i[0])
f.sort()
for i in f:
    print(i)
