a=int (input())
n=0

if (a%2==0):
    b=a+1
    print (b)
    for i in range (5):
        b+=2
        print (b)
else:
    if(a%2!=0):
        print (a)
        for i in range(5):
            a+=2
            print (a)
