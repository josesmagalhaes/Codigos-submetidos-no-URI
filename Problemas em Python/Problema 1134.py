comb=0
x=0
y=0
z=0

while (x!=4):
    comb = int(input())
    if (comb==4):
        break
    else:
        if (comb == 1):
            x+=1
        elif (comb == 2):
            y+=1
        elif (comb == 3):
            z+=1
        else:
            continue

print ("MUITO OBRIGADO")
print ("Alcool: %d"%x)
print ("Gasolina: %d"%y)
print ("Diesel: %d"%z)
