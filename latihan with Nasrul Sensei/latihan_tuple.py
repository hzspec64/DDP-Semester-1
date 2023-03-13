#membuat tuple
ar_buah = ("Pepaya", "Mangga", "Pisang", "Jambu", "Belimbing", "Naga")
print("--------Cetak perbuah--------")
print("Buah dengan index 3 buah",ar_buah[3])
print("Buah dengan index 5 buah",ar_buah[5])
print("--------all buah--------")
for buah in ar_buah:
    print("buah",buah)
print("--------memotong tuple--------")
print("Potong list antara index 1 s/d index 5",ar_buah[1:5])