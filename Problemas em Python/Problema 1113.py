x=1
y=0
while (x!=y):
    entrada = input().split()
    x = int(entrada[0])
    y = int(entrada[1])

    if (x>y):
        print("Decrescente")
    elif(x<y):
        print ("Crescente")
