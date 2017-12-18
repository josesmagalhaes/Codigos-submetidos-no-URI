tempo_gasto = float(input ("Digite o tempo gasto: "))
velocidade_media = float(input ("Digite a velocidade media: "))

distancia_percorrida = tempo_gasto*velocidade_media
litros_gastos = distancia_percorrida/12;

print ("O valor da quantidade de litros necessarios e: %.3f"%litros_gastos)