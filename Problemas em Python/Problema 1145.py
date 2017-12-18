entrada = input()
x = int(entrada.split()[0])
y = int(entrada.split()[1])
a = " "
c = 0
for i in range(1, y + 1):
    print("%i%s" % (i, a), end="")
    c += 1
    if c == x:
        print("")
        c = 0
