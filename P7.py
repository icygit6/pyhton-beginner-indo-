i = 0
while True :
    umur = int (input ('Umur = '))
    print ('apakah anda meguasai bahasa pemrograman?')
    jwb = input ('jawab: ')
    if (umur >= 20 and umur <= 25 and jwb == 'iya'):
       i = i + 1
       if (i == 5):
           print ('total: ',i,'/5')
           break
    print ('total: ', i,'/5')
          
            
            
  

