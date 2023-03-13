def hitungUmur(tahun_ini):
    nama = input('Nama Siswa : ')
    tahun = int(input('Tahun Lahir: '))
    umur = tahun_ini - tahun
    print("Siswa dgn nama %s yg lahir pada tahun %i berumur %i tahun" 
        %(nama,tahun,umur))  
print('Data diri anda')
hitungUmur(2022)