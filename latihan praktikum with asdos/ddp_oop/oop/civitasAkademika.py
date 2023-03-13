from dosen import *
from mahasiswa import *

# membuat object
d1 = Dosen("Tifani Nabarian","P",35,"S.Kom M.T.I","Kaprodi IT")
d2 = Dosen("Nasrul","P",40,"S.Kom M.Kom","Instruktur NFCOM")
m1 = Mahasiswa("Jasrino","L",19,"Sistem Informasi",1)
m2 = Mahasiswa("Dewi","P",18,"Teknologi Informasi",2)

# memakai method setGaji dan Cetak
d1.setGaji(15000000)
d2.setGaji(12000000)

d1.cetak()
d2.cetak()
m1.cetak()
m2.cetak()