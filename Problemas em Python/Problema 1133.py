x=int(input())
y=int(input())
i=0

if (x<y):
    for i in range (x+1,y):
        if ((i%5)== 2) or ((i%5)==3):
            print (i)
elif (y<x):
    for i in range (y+1,x):
        if ((i%5)== 2) or ((i%5)==3):
            print (i)