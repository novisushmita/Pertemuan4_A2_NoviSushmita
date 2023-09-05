a = int(input())
b = int(input())
c = int(input())

if(a>b):
    if(c>a):
        print(a)
    elif(c>b):
        print(b)
else:
    if(c>b):
        print(b)
    elif(c>a):
        print(c)