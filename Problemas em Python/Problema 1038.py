codigo = int(input ("Digite o codigo do produto: "))
quantidade = int(input ("Digite a quantidade de produtos: "))

if (codigo == 1):
    valor = (int(quantidade)*4.00)
elif (codigo == 2):
    valor = (int(quantidade)*4.50)
elif (codigo == 3):
    valor = (int (quantidade)*5.00)
elif (codigo == 4):
    valor = (int (quantidade)*2.00)
elif (codigo == 5):
    valor = (int(quantidade)*1.50)

print ("O valor e: %.2f"%valor)