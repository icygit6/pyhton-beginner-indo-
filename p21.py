class jen:
    def __init__(self,jenis):
        self.jenis = jenis
class he(jen):
    def __init__(self,nama,umur,berat,jenis):
        super().__init__(jenis)
        print ('identitas hewan')
        print('nama:',nama)
        print('umur:',umur)
        print('berat:',berat)
        print('jenis:',jenis)
  
hew = he('kucing','12 tahun','12 kg','mamalia')
dog = he ('anjing','10 tahun','10kg','mamalia')
