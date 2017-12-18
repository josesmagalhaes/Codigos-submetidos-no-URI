n1= int(input())
n2= int(input())
n3= int(input())
n4= int(input())
n5= int(input())

lista = [n1, n2, n3, n4, n5]

i = 0
pares = 0
while (i < len(lista)):
    if (lista[i] % 2 == 0):
        pares = pares + 1

    i = i + 1

print ("%d valores pares" % pares)