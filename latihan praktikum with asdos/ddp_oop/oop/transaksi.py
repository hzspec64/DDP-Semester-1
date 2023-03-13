from bank import *

# membuat object
dimasAji = Bank("004", "Dimas Aji Nugroho", 7500000)
dimasJulian = Bank("215", "Dimas Julian", 500000)
jasrino = Bank("214", "Jasrino Maulana Putra", 15000000)
hafiizh = Bank("011", "Hafiizh Wahyu Alamsyah", 4000000)
pakdeli = Bank("164", "Fahdeli Nugroho", 300000)
hamzah = Bank("043", "Hamzah Abdullah", 50000000)

# memakai method
dimasJulian.nabung(10000000)
dimasAji.nabung(5000)
jasrino.tarik(7500000)
hafiizh.tarik(500)
hamzah.nabung(20000000)
hamzah.tarik(6969696969)

# memakai method cetak
dimasAji.cetak()
dimasJulian.cetak()
jasrino.cetak()
hafiizh.cetak()
hamzah.cetak()