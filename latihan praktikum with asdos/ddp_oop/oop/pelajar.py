from orang import *

class Pelajar(Orang):
    # variabel kosong
    sekolah = ""

    # membuat attribute
    def __init__(self, nama, asal, sekolah):
        super().__init__(nama, asal)
        self.sekolah = sekolah

    # membuat method
    def bersekolah(self):
        super().doPerkenalan()
        print("Saya bersekolah di",self.sekolah)