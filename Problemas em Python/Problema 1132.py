x=int(input())
y=int(input())
i=1
soma=0

if (x<y):
    for i in range(x,y+1):
        if ((i%13)!=0):
            soma+=i
    print(soma)
elif (y<x):
    for i in range(y,x+1):
        if ((i%13)!=0):
            soma+=i
    print(soma)