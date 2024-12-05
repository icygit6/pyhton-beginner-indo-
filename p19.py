class anggotasekolah:
    #'representasi anggota sekolah'
    def __init__(self,nama,umur):
        self.nama = nama
        self.umur= umur
        print ('membuat anggota skolah baru: %s'%self.nama)
    def info (self):
        #'cetak info'
        print ('Nama: %s, umur:%s' %(self.nama, self.umur))
class guru(anggotasekolah):
    #'representasi guru'
    def __init__(self,nama,umur,gaji):
        super().__init__(nama,umur)
        self.gaji = gaji
        print ('nama guru: %s' % self.nama)
        print('umur: %s' % self.umur)
        print ('gaji: %s' % self.gaji)
    def info (self):
        anggotasekolah.info(self)
        print ('gaji: %s' %self.gaji)
class siswa(anggotasekolah):
    #'representasi siswa'
    def __init__(self,nama,umur,nilai):
        super().__init__(nama,umur)
        self.nilai = nilai
        print ('Nama siswa: %s' %self.nama)
        print ('umur: %s' % self.umur)
        print ('nilai: %s' % self.nilai)
    def info (self):
        anggotasekolah.info(self)
        print ('nilai: %s' %self.nilai)
gu = guru ('budi',40,3000000)
si = siswa ('andi',25,75)
class computer ():
    def __init__(self,com,ram,stor):
        self.com = com
        self.ram= ram
        self.stor = stor
class mobile(computer):
    def __init__(self,com,ram,stor,model):
        super().__init__(com,ram,stor)
        self.model = model
apple = mobile('apple',2,64,'iphone x')
print ('the mobile is',apple.com)
print ('the ram is', apple.ram)
print ('the strorage is', apple.stor)
print ('the model is', apple.model)
