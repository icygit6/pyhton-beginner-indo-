while True:
    k = input('kelas:')
    if (k =='a'):
        a= 4000000
        print ('gaji: Rp.',a)
        j = int(input('jam:'))
        t = j*50000
        to= a+t
        print('total: Rp.',to)
    if(k == 'b'):
        b= 3000000
        print('gaji: Rp.',b)
        j = int(input('jam:'))
        t = j*35000
        to = b+t
        print('total: Rp.',to)
    if(k == 'c'):
        c= 2500000
        print('gaji: Rp.',c)
        j = input('jam:')
        t = j*20000
        to = c+t
        print('total: Rp.',to)
    if (k =='0'):
        break
