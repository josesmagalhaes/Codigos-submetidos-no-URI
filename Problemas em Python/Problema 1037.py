valores = float(input())

if valores < 0:
	print("Fora de intervalo")
elif 0 <= valores <= 25.00:
	print("Intervalo [0,25]")
elif 25.01 <= valores <= 50.00:
	print("Intervalo (25,50]")
elif 50.01 <= valores <= 75.00:
	print("Intervalo (50,75]")
elif 75.01 <= valores <= 100.00:
	print("Intervalo (75,100]")
else:
	print("Fora de intervalo")