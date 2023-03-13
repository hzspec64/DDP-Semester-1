#----------Membuat dictionary----------
ar_nilai = {"Budi":75, "Dewi":55, "Ani":95, "Bedu":30}
print("----------cetak key nya saja----------")
for siswa in ar_nilai.keys():
    print("Siswa",siswa)

print("----------cetak value nya saja----------")
for nilai in ar_nilai.values():
    print("Nilai",nilai)

print("----------cetak key dan value nya sekaligus----------")  
for nama,nilai in ar_nilai.items():
    print("Siswa bernama",siswa,"Nilainya",nilai)