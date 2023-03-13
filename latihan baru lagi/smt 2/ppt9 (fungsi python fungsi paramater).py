def hitungGaji():
    #-----------input data--------
    nama = input('Masukkan nama \t\t:')
    jabatan = input('Masukkan Jabatan \t:')
    agama = input('Masukkan agama \t\t:')
    jumlah = int(input('Masukkan Jumlah Anak \t:'))
    #------tentukan gapok----------
    def gapok(jabatan):
        return{
            "General Manager":20000000,
            "Manager": 10000000,
            "Staff": 5000000
        }[jabatan]

#-----------tunjangan anak------------
    persen = 0.01
    if(jumlah > 0 and jumlah < 4):
        tunak = gapok(jabatan) * persen * jumlah
    elif(jumlah > 3):
        tunak = gapok(jabatan) * persen * (jumlah-(jumlah-3))
    else:
        tunak = 0
    #------------zakat profesi-------------------
    gaji_kotor = gapok(jabatan) + tunak 
    zakat = (0.025 * gaji_kotor) if gaji_kotor >= 10000000 and agama == "Islam" else 0

    gaber = (gapok(jabatan) + tunak) - zakat

#--------cetak populasi data---------
    print('\n\n-------Data Pegawai----------'
        '\nNama Pegawai\t\t:', nama,
        '\nJabatan\t\t\t:',jabatan,
        '\nAgama\t\t\t:',agama,
        '\nJumlah Anak \t\t:',jumlah,
        '\nGaji Pokok \t\t:',gapok(jabatan),
        '\nTunjangan Keluarga \t:',tunak,
        '\nZakat Profesi \t\t:',zakat,
        '\nTake Home Pay \t\t:',gaber,
        )
#jalankan program
print('\n\n---------Input Data Pegawai----------')
hitungGaji()
