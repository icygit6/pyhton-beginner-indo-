class ling:
    def __init__(self,jari):
        self.jari = jari 
    def luas(self):
        luli = 22/7*(self.jari*self.jari)
        print (luli)
L = ling (7)
L.luas()
class balok:
    def __init__(self,p,l,t):
        self.p= p
        self.l= l
        self.t= t
    def luper(self):
        lp = 2*((self.p*self.l)+(self.p*self.t)+(self.l*self.t))
        print ('luas balok=',lp)
lup= balok(2,4,8)
lup.luper()
class tabung:
    def __init__(self,r,t):
        self.r= r
        self.t= t
    def lupe(self):
        lpt = 2*(22/7*(self.r*self.r))+2*(22/7*self.r*self.t)
        print ('luas tabung =',lpt)
lt= tabung (2,4)
lt.lupe()
