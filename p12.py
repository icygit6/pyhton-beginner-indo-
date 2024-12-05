n= int(input('n= '))
def fibo(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
print (fibo(n))
a= int(input('b1= '))
b= int(input('b2= '))
def kali(a,b):
    if b==1:
        return a
    else:
        return a + kali(a,b-1)
print(kali(a,b))
