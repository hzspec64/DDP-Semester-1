nama = "Budi Santoso"
produk = "AC"
jumlah = 3
harsat = 5000000
#uji diskon 20% minimal jumlah 2 dan produknya TV dengan Tuple & List
diskon = (0, 0.2)[produk == "TV" and jumlah >= 2]

hator = jumlah * harsat
habar = hator - diskon 
#cetak
print("Nama Pelanggan\t:",nama,
     "\nProduk Beli\t:",produk,
     "\nHarga Kotor\t:",hator,
     "\nDiskon\t\t:",diskon,
     "\nHarga Bayar\t:",habar
)