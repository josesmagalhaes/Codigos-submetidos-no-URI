y=float(0)
z=float(0)
media=float(0)

while(1):
    x=float(input())
    if (x<0)or(x>10):
        print("nota invalida")
    elif (z==0):
        y=x
        z=1
    else:
        media=(y+x)/2
        print("media = %.2f"%media)