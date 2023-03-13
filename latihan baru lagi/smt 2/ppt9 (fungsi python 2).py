def infoSuhu():
    lokasi = input('Masukkan Lokasi\t: ')
    suhu = int(input('Masukkan Suhu\t: '))
    #-------buat fungsi status suhu--------
    def status():
        if(suhu <= 0 ):
            kondisi = 'Beku'
        elif(suhu > 0 and suhu <= 16):
            kondisi = 'Dingin'
        elif(suhu > 16 and suhu <= 20):
            kondisi = 'Sejuk'
        elif(suhu > 20 and suhu <= 30):
            kondisi = 'Biasa'
        else:
            kondisi = 'Panas'

        return kondisi		

#--------cetak populasi data---------
    print('\n---------------Informasi Suhu---------------'
          '\nLokasi\t:',lokasi,
          '\nSuhu\t:',suhu,
          '\nKondisi\t:',status())

#jalankan program
print('\n\n-------Informasi Suhu di Suatu Daerah-------')
infoSuhu()