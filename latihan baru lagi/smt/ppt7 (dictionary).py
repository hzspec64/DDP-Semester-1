nilai = {'Firda':89, 'Inaya':100, 'Deden':59,'Fawwaz':95}
nilai["Deden"] = 60
print("Data nilai : ",nilai)
print("\n------------cetak valuenya saja---------------------\n")
#cetak nilai saja
for skor in nilai.values():
    print("Data Nilai : ",skor)
print("\n------------cetak key aja---------------------\n")

#cetak nama saja
for nama in nilai.keys():
    print("Data Siswa : ",nama)
print("\n------------cetak key dan values------------------\n")

#cetak key dan value secara bersamaan / manual
for nama,skor in nilai.items():
    print("Nama Siswa : %s \t Nilai : %i" % (nama,skor))    