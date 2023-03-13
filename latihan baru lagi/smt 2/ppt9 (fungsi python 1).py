def hitungUmur(tahun_ini):
    nama = input('Nama Siswa\t: ')
    tahun = int(input('Tahun Lahir\t: '))
    umur = tahun_ini - tahun
    print("Siswa dgn nama %s yg lahir pada tahun %i berumur %.2f tahun" %(nama,tahun,umur))
print('Data diri anda')
hitungUmur(2022)