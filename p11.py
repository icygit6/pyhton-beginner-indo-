n= int(input('num: '))
def faktorial(n):
    if n==1:
        return 1
    else:
        print(n)
        return n * faktorial(n-1)
print ('val= ',n,'adalah= ', faktorial(n))
