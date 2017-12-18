entrada =0
entrada = input().split()
p1 = int(entrada[0])
c1 = int(entrada[1])
p2 = int(entrada[2])
c2 = int(entrada[3])

if (p1*c1)==(p2*c2):
    print("0")
elif (p1*c1)>(p2*c2):
    print("-1")
else:
    print("1")