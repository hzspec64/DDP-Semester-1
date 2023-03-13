#=========List Data Mahasiswa========
masis1 = {"NIM":111,"Nama":"Budi","Nilai":77}
masis2 = {"NIM":112,"Nama":"Siti","Nilai":96}
masis3 = {"NIM":113,"Nama":"I Gede","Nilai":55}
masis4 = {"NIM":114,"Nama":"Joko","Nilai":25}
masis5 = {"NIM":115,"Nama":"Ahmad","Nilai":85}

print("=====================================================",
    "\n-------List Data Mahasiswa Karakura University-------",
    "\n====================================================="
    )

nim = int(input("Masukkan NIM\t: "))
namae = input("Masukkan Nama\t: ")
score = float(input("Masukkan Nilai\t: "))
ket = "%s"
grade = "%s"
predi = "%s"

#=========Input Data score Mahasiswa========
ket = ("Gagal","Lulus")[score >= 60]
if(score >= 85 and score <= 100):
    grade = "A"
    predi = "Memuaskan"
elif(score >= 75 and score < 85): 
    grade = "B"
    predi = "Bagus"
elif(score >= 60 and score < 75): 
    grade = "C"
    predi = "Cukup"
elif(score >= 30 and score < 60): 
    grade = "D"
    predi = "Kurang"
elif(score >= 0 and score <= 30):
    grade = "E"
    predi = "Buruk"
else:
    grade = "Tidak Ada"
    predi = "Tidak Ada"

print(""
      "\n-----Hasil Data Nilai-----"
      "\n=========================="
      "\nNIM\t\t: %i"
      "\nNama\t\t: %s"
      "\nNilai\t\t: %.2f"
      "\nKeterangan\t: %s"
      "\nGrade\t\t: %s"
      "\nPredikat\t: %s"
      "\n=========================="
      %(nim,namae,score,ket,grade,predi)
    )