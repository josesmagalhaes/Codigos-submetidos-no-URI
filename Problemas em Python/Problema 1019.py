tempo = int(input())
segundo = int(tempo % 60)
minutos = int((tempo / 60)% 60)
hora = int(tempo / 3600 )
print("%.i:%.i:%.i" % (hora,minutos,segundo))