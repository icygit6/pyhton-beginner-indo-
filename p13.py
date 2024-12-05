b = int (input('b= '))
def funpara(b):
    p = 0
    j= 0
    for i in range (0,b):
        n= int(input('n= '))
        p= p+n
        j= p/b
    return p,j
print ('total,rata2:',funpara(b))

n= int(input('n='))
def f(bat):
    j = 1
    for i in range (bat,1,-1):
        print (i)
        j = j * i
    return j
print (f(n))
