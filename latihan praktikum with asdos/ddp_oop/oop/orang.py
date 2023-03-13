class Orang:
    # variabel kosong
    nama = ""
    asal = ""

    # attribute (identitas) atau fungsi constructor
    def __init__(self,nama,asal):
        self.nama = nama
        self.asal = asal

    # method (perilaku)
    def doPerkenalan(self):
        print("Haloo perkenalkan saya",self.nama,"saya berasal dari",self.asal)