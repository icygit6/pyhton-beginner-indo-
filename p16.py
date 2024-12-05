class maram:
    cakra = 'Halo Cakra'
    Turi = 'hai turi'
    x= 10
print (maram.cakra)
print (maram.Turi)
print (maram.x)
class person:
    nama=''
    def __init__(self,nama):
        self.nama = nama
        print (self.nama)
person = person('adi')
class Car :
    def start(self):
        print('engine started')
car_a = Car()
car_a.start()
class car1:
    def start ():
        message = 'Engine starter'
        return message
class car2 :
    message1= 'car starter'
    def start ():
        message2 = 'engine started'
        return message2
car_b= car1
print(car_b.start())
car_c =car2
print (car_c.message1)
print (car_c.start())
class mahasiswa:
    def __init__(self,nama,nim,prodi,thn_masuk):
        self.nama= nama
        self.nim= nim
        self.prodi= prodi
        self.thn_masuk= thn_masuk
m1= mahasiswa('udin','1020304','sistem informasi',2020)
teks = '%s adalah mahasiswa %s angkatan %d dengan nim %s' %(m1.nama,m1.prodi,m1.thn_masuk,m1.nim)
print (teks)
