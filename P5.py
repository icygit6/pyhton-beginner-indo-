angka = 1
p = 0
n = -1
ge = -1 
ga = 0
while (angka != 0):
    angka = int (input ('Angka = '))
    if(angka > 0):
       p = p + 1
    else:
       n = n + 1
    if(angka % 2 ==0 ):
        ge = ge + 1
    else:
        ga = ga + 1
print ('Positif = ',p )       
print ('Negatif = ',n)
print ('Genap = ',ge)
print ('Ganjil = ', ga)

    

