n=int(input())
i=1
soma=0
for i in range (0,n):
    entrada=input().split()
    x=int(entrada[0])
    y=int(entrada[1])
    for i in range (x,y):
        if ((i%2)!=0):
            soma+=i

    print (soma)
