a=int (input(""))
n=0
dentro=0
fora=0

for i in range(0,a):
    b = int(input(""))
    if ((b>=10) and (b<=20)):
        dentro += 1
    elif ((b<10) or (b>20)):
        fora+=1

print (dentro,'in')
print (fora,'out')
print (a)