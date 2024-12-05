import math
n= [34.6,-203.5,44.9,68.3,-12.2,44.6,12.7]
k= []
b= 0
for i in n:
    a = math.ceil(i)
    b = a + b
    k.append(a)
print(k[::])
print('jumlah:',b)
