entrada = input().split()
st = int(entrada[0])
sm = int(entrada[1])
et = int(entrada[2])
em = int(entrada[3])

rt = et-st
if(rt<0):
    rt = 24 + (et-st)

rm = em-sm
if (rm < 0):
    rm = 60 + (em-sm)
    
elif ((et==st)and(em==sm)):
    print("O JOGO DUROU 24 HORA(S) E 0 MINUTOS(S)")
else:
    print('O JOGO DUROU',rt,'HORA(S) E',rm,'MINUTO(S)')