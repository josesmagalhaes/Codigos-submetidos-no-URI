x=0
y=0
while (1):
    entrada = input().split()
    x = int(entrada[0])
    y = int(entrada[1])

    if (x==0) or (y==0):
        break

    if (x>0)and(y>0):
        print("primeiro")
    elif (x<0)and(y>0):
        print ("segundo")
    elif (x<0)and(y<0):
        print ("terceiro")
    elif (x>0)and(y<0):
        print("quarto")