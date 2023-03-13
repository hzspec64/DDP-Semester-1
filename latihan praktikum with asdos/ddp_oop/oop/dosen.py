from person import *

class Dosen(Person):
    # variabel kosong gelar, jabatan, gaji
    gelar = ""
    jabatan = ""
    gaji = 0

    # membuat attribute yang juga diambil dari parent class
    def __init__(self,nama,gender,umur,gelar,jabatan):
        super().__init__(nama, gender, umur)
        self.gelar = gelar
        self.jabatan = jabatan

    # membuat method setGaji dan cetak
    def setGaji(self,uang):
        self.gaji = self.gaji + uang
    
    def cetak(self):
        super().cetak()
        print("Gelar\t\t :",self.gelar,
              "\nJabatan\t\t :",self.jabatan,
              "\nGaji\t\t :",self.gaji
            )