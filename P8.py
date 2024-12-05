contoh = [1,'SCC',6.75]
print(contoh[2])
print (contoh[0:3])
for i in contoh:
    print (i)
num = [1,-2,3,4,5,-6,-7,8,-9,-10]
print (num[0:11:3])
for p in num :
    if (p <= 0 ):
        print(p)
n= [['kopi','susu'],
    ['jus apel','jus melon'],
    ['eskopi','es campur']]
print (n[2][1])
print (len(n))
A = int(input('A = '))
B = int (input('B = '))
C = int (input('C = '))
l = [A,B,C]
print (l[::])
bil = [6,3,22,7,8]
print (max(bil))
print (min(bil))
an=[6,3,6,2]
inp = int(input('Input = '))
print ('Total= ',an.count(inp))
u =0
pro= []
while True :
    b1= (input('b= '))
    pro.append(b1)
    u = u + 1
    if (u== 5):
        print(pro[::])
        print('Total: ',len(pro))
        print('ok')
        break
  
