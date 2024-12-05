class data:
    def __init__(self):
       self.n= []
       self.a = []
       self.no = []
       self.em= []
    def add(self,b):
        for i in range(0,b):
            na= input('nama= ')
            self.n.append(na)
            al= input('alamat= ')
            self.a.append(al)
            nom = input('nomor telepon= ')
            self.no.append(nom)
            ema = input('email= ')
            self.em.append(ema)
    def tam(self,t):
        for i in range (0,t):
            print('identitas',t,':\n','nama: ',self.n[i],'\n','alamat: ',self.a[i],
                  '\n','nomor telepon: ',self.no[i],'\n','email: ',self.em[i])

da = data()
da.add(2)
da.tam(2)
