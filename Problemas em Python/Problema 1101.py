m=1
n=1

while (m>0) and (n>0):
    entrada = input().split()
    m = int(entrada[0])
    n = int(entrada[1])

    soma=0
    if (m<=0):
        break
    elif (n<=0):
        break

    if (m>n):
        for i in range (n,m+1):
            print(i,end=' ')
            soma+=i
        print("Sum=%d"%soma)

