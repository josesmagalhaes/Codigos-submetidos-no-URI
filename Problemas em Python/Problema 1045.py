entrada = input().split()
A = float(entrada[0])
B = float(entrada[1])
C = float(entrada[2])

if ((A>= (B+C)) or (B>=(A+C)) or(C>=(A+B))):
    print ("NAO FORMA TRIANGULO")
elif((A*A)==(B*B)+(C*C)) or ((B*B)==(A*A+C*C)) or ((C*C)==(A*A+B*B)):
    print ("TRIANGULO RETANGULO")
elif((A*A)>(B*B)+(C*C)) or ((B*B)>(A*A+C*C)) or ((C*C)>(A*A+B*B)):
    print ("TRIANGULO OBTUSANGULO")
elif((A*A)<(B*B)+(C*C)) or ((B*B)<(A*A+C*C)) or ((C*C)<(A*A+B*B)):
    print ("TRIANGULO ACUTANGULO")
if ((A==B)and A==C):
    print ("TRIANGULO EQUILATERO")
if ((A==B)and (A != C)) or ((B==C) and (B!=A)) or ((A==C)and (A!=B)):
    print ("TRIANGULO ISOSCELES")