entrada = input().split()
a = int(entrada[0])
b = int(entrada[1])
rt = b-a
if(rt<0):
    rt = 24 + (b-a)
    print('O JOGO DUROU',rt,'HORA(S)')
elif (a == b):
    print("O JOGO DUROU 24 HORA(S)")
else:
    print('O JOGO DUROU',rt,'HORA(S)')