p = int(input('panjang='))
l = int(input('lebar='))
class LK :
    def __init__(self,p,l):
        self.p= p
        self.l= l
    def lp(self):
        Lp = p*l
        print('Luas persegi = ',Lp)
    def kp(self):
        Kp = 2*(p+l)
        print('Keliling persegi= ',Kp)
Lu= LK(p,l)
Lu.lp()
Ke = LK(p,l)
Ke.kp()


