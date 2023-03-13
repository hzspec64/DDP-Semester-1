list_makanan = [
    ["Bakwan", "Combro", "Misro"],
    ["Sop Iga", "Sop Ayam", "Sop Kambing"],
    ["Nasi Uduk", "Nasi Goreng", "Nasi Rames"],
]
print("----------cetak per item----------")
print("Makanan index[0][0]",list_makanan[0][0])
print("Makanan index[1][1]",list_makanan[1][1])
print("Makanan index[2][1]",list_makanan[2][1])
print("----------cetak semua element list----------")

for menu in list_makanan:
    for makanan in menu:
        print(makanan)