#----------Membuat dictionary----------
s1 = {"Budi":75,"Matpel":"Matematika"}
s2 = {"Dewi":55,"Matpel":"IPA"}
s3 = {"Ani":95,"Matpel":"IPS"}
s4 = {"Bedu":30,"Matpel":"Agama"}

#----------Masukkan data ke list----------
ar_siswa =[s1,s2,s3,s4]

#----------Cetak daftar nilai dengan Nested Loop----------
for siswa in ar_siswa:
    for key, data in siswa.items():
        #----lulus jika nilai minimal 60----
        skor = key == "nilai"
        ket = ("Gagal", "Lulus"),[ skor >= 60]
        print(key,data)