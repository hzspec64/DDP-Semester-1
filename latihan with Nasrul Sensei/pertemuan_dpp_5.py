#membuat list
ar_buah = ["Pepaya", "Mangga", "Pisang", "Jambu", "Belimbing"]
#ubah element list index 2 (Pisang diubah menjadi Apel)
ar_buah[2] = "Apel"
print ("Buah index 2 adalah buah",ar_buah[2])
del ar_buah[4] #hapus buah index 4 (Belimbing)
#print("Buah index 4 adalah buah",ar_buah[4])
#looping list buah
for buah in ar_buah:
    print("Buah",buah)

print("----------menambah elemen list----------")
ar_buah.insert(1, "Naga")
ar_buah.append("Jeruk")
#looping list buah
for buah in ar_buah:
    print("Buah",buah)