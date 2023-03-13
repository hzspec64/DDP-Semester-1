nama = "Megumin"
matpel = "Pemrograman Web"
nilai = 98
#menguji nilai Megumin apakah lulus atau tidak

if(nilai >= 85 and nilai <=100):
    grade = "A"
elif(nilai >= 75 and nilai <=85):
    grade = "B"
elif(nilai >= 65 and nilai <=75):
    grade = "C"
elif(nilai >= 55 and nilai <=65):
    grade = "D"
elif(nilai >= 30 and nilai <=55):
    grade = "E"
else: 
    grade = "F"

print("Nama Siswa\t:",nama,
      "\nMata Pelajaran\t:",matpel,
      "\nNilai\t\t:",nilai,
      "\nGrade\t\t:",grade
)