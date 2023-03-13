# input output

#input
nama = "Luffy"
umur = 19
nilai = 90.78

#output
# menggunakan print()

#cara print standar
print("Nama saya:",nama)
print("Nama saya:",nama,"umur saya:",umur,"nilai saya:",nilai)

print("=============================================================")

#cara menggunakan format print
print("Nama saya: %s" %(nama))
print("Nama saya: %s umur saya adalah %i nilai saya sebesar %.2f" %(nama,umur,nilai))

#input
#menggunakan fungsi input()
# fungsi input () akan menghasilkan tipe data string, jadi jika ingin tipe data lain harus 
# dikonversi

nama = input("Masukkan nama :")
umur = int(input("Masukkan umur :"))
nilai = float(input("Masukkan nilai :"))
