A = int(input('A = '))
B = int (input('B = '))
C = int (input('C = '))
if (A > B  and A > C):
    print ('max = A =',A)
if(B > A and B > C):
    print ('max = B =',B)
if (C > A and C > B ):
    print ('max = C =',C)
g = input ('Golongan = ')
nama = input('Nama = ')
gaji = int (input('Gaji = '))
ba = gaji*0.2
ta = ba+gaji
bb = gaji*0.15
tb = bb+gaji
bc = gaji*0.1
tc = bc+gaji
if(g == 'A'):
   print ('Nama = ', nama,'\nBonus = ',ba, '\nTotal = ',ta)
if (g == 'B'):
   print ('Nama = ', nama,'\nBonus = ', bb, '\nTotal = ',tb)
if (g == 'C'):
   print ('Nama = ', nama,'\nBonus = ', bc,'\nTotal = ',tc)
