class Mobil:
    # membuat attribute (identitas)
    def __init__(self, roda, tipe, kecepatan):
        self.roda = roda
        self.tipe = tipe
        self.kecepatan = kecepatan

    #membuat method (perilaku)
    def doMelaju(self):
        print("Melaju dengan kecepatan :",self.kecepatan,"km/jam")
    
    def doKlakson(self):
        print("Melakukan klakson")
    
    def doBelok(self):
        print("Belok ke arah")