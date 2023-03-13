from configparser import MAX_INTERPOLATION_DEPTH


pelanggan = "Tokisaki Kurumi"
TotalBelanja = 500000

if(TotalBelanja > 200000):
    keterangan = "Selamaatt Anda Mendapatkan Hadiah"
else: 
    keterangan = "Terima Kasih Telah Berbelanja"

print("Pelanggan:\t\t",pelanggan,
      "\nTotal Belanja Anda:\t Rp.",TotalBelanja,
      "\n",keterangan
     )

