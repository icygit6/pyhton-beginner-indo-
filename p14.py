a= int (input ('a= '))
n= []
def med(a):
    for i in range (0,a):
        i = int(input('n= '))
        n.append(i)
    if (a % 2 == 0 ):
        k= a//2
        l= a//2-1
        b= (n[k] + n[l])/2
        print (b)
    else:
        m= (a//2)
        print (n[m])
        print(n)
med(a)
        
