def hitungUmur(tahun_ini):
    namae = input("Nama Anda\t: ")
    tahun_lahir = int(input("Tahun Lahir\t: "))
    age = tahun_ini - tahun_lahir
    print("Siswa dengan nama %s yang lahir pada tahun %i berumur %i tahun" %(namae,tahun_lahir,age))

hitungUmur(2022)