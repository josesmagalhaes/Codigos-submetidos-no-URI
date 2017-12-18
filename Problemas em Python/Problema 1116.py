x=0
y=0
i=0
n=int(input())

for i in range (0,n):
    entrada = input().split()
    x = int(entrada[0])
    y = int(entrada[1])

    if (x==0):
        break

    if (y==0):
        print("divisao impossivel")
    else:
        print(float(x)/float(y))

