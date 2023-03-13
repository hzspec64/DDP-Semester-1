from orang import *
from pelajar import *

class Pekerja(Orang):
    # variabel kosong tempat_kerja
    tempat_kerja = ""

    # membuat attribute yang diambil dari parent class
    def __init__(self,nama,asal,tempat_kerja):
        super().__init__(nama, asal)
        self.tempat_kerja = tempat_kerja

    # membuat method bekerja
    def bekerja(self):
        super().doPerkenalan()
        print("Saya bekerja di", self.tempat_kerja)