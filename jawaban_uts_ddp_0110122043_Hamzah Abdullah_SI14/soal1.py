#=========List Data Pelanggan========
p1 = {"Nama":"Budi","Produk":"TV","Jumlah":3}
p2 = {"Nama":"Ani","Produk":"AC","Jumlah":4}
p3 = {"Nama":"Siti","Produk":"Kulkas","Jumlah":2}
p4 = {"Nama":"Dewi","Produk":"AC","Jumlah":5}
p5 = {"Nama":"Andi","Produk":"Kulkas","Jumlah":7}
p6 = {"Nama":"Dedi","Produk":"AC","Jumlah":1}
p7 = {"Nama":"Sri","Produk":"TV","Jumlah":4}
ar_pelanggan = [p1,p2,p3,p4,p5,p6,p7]

print("=====================================================",
    "\n-----List Data Pelanggan Beliau Aizen Mart (BAM)-----",
    "\n====================================================="
    )
for pelanggan in ar_pelanggan:
    for key, data in pelanggan.items():
        print("|",key,":",data)

#=========Data Harga Produk==========
        ha = pelanggan["Produk"]
        if ha == "Kulkas":
            hasu = 7000000
        elif ha == "AC":
            hasu = 6000000
        else:
            hasu = 5000000
        hako = pelanggan["Jumlah"] * hasu
        disk = (0.05 * hako, 0.2 * hako)[pelanggan["Produk"] == "Kulkas" and pelanggan["Jumlah"] >= 3]
        hsd = hako - disk
        p2n = 0.11 * hsd
        haby = hako + p2n - disk 
    print("| Harga Satuan\t: Rp.",hasu,
          "\n| Harga Kotor\t: Rp.",hako,
          "\n| Diskon\t: Rp.",disk,
          "\n| PPN\t\t: Rp.",p2n,
          "\n|________________________________"
          "\n| Harga Bayar\t: Rp.",haby,
          "\n|================================"
          "\n"
        )
