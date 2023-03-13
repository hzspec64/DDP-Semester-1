from mobil import *

# membuat object
mobilBus = Mobil(8, "Transportasi", 150)
mobilTesla = Mobil(4, "Listrik", 250)
mobilLambo = Mobil(4, "Sport", 450)
mobilRubicon = Mobil(4, "Jeep", 120)
mobilAlphard = Mobil(4, "Transportasi", 140)

# mencetak output
print(mobilTesla.tipe)
print(mobilLambo.tipe)
print(mobilBus.tipe)

print("=====================================")

# memakai method
mobilRubicon.doMelaju()
mobilAlphard.doMelaju()
mobilBus.doMelaju()

print("=====================================")