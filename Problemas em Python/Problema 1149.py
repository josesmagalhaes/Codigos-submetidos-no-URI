e = input().split()
a = int(e[0])
b = int(e[len(e)-1])
soma = 0
for i in range(a, (a + b)):
    soma+=i
print(soma)