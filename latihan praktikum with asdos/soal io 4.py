namae = str(input("Masukkan Nama\t: "))
tl = str(input("Masukkan Tempat Lahir: "))
genre = str(input("Masukkan Jenis Kelamin\t: "))
toshi = int(input("Masukkan Umur\t: "))
goldar = str(input("Masukkan Golongan Darah\t: "))
height = float(input("Masukkan Tinggi\t: "))
weight = float(input("Masukkan Berat Badan\t: "))

print("_____________________________________________",
      "Nama\t\t: %s",
      "Tempat Lahir\t: %s",
      "Jenis Kelamin\t: %s",
      "Umur\t\t: %i",
      "Golongan Darah\t: %s",
      "Tinggi\t\t: %.2f"
      "Berat Badan\t: %.2f"
      %(namae,tl,genre,toshi,goldar,height,weight)
      )