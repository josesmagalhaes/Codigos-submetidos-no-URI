a = float(input(""))
if ((a>=0)and(a<=400.00)):
    a1g=a*0.15
    a1=a1g+a
    print("Novo salario: %.2f" % a1)
    print("Reajuste ganho: %.2f" % a1g)
    print("Em percentual: 15 %")
elif ((a>=400.01)and(a<=800.00)):
    a1g = a * 0.12
    a1 = a1g + a
    print("Novo salario: %.2f" % a1)
    print("Reajuste ganho: %.2f" % a1g)
    print("Em percentual: 12 %")
elif ((a>=800.01)and(a<=1200.00)):
    a1g = a * 0.10
    a1 = a1g + a
    print("Novo salario: %.2f" % a1)
    print("Reajuste ganho: %.2f" % a1g)
    print("Em percentual: 10 %")
elif ((a>=1200.01)and(a<=2000.00)):
    a1g = a * 0.07
    a1 = a1g + a
    print("Novo salario: %.2f" % a1)
    print("Reajuste ganho: %.2f" % a1g)
    print("Em percentual: 7 %")
elif (a>2000.01):
    a1g = a * 0.04
    a1 = a1g + a
    print("Novo salario: %.2f" % a1)
    print("Reajuste ganho: %.2f" % a1g)
    print("Em percentual: 4 %")