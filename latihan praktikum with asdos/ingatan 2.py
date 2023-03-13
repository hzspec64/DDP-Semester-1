# kondisional if else
# konsep sederhananya adlaah jika-maka & selain itu

# jika jumlah mahasiswa dalam satu kelas lebih dari 19, maka itu adalah kelas si 14
# selain itu bukan kelas si 14

jumlah_mahasiswa = 14

if jumlah_mahasiswa >= 19:
    print('Ini adalah Kelas SI 14')
else:
    print('Bukan Kelas SI 14')

# jika praktikum dilaksanakan pada hari senin, maka itu adalah praktikum ddp
# jika praktikum dilaksanakan pada hari rabu, maka itu adalah praktikum web
# jika praktikum dilaksanakan pada hari jumat, maka itu adalah praktikum front end
# selain itu adalah kelas literasi

praktikum = 'Jumat'

if praktikum == 'Senin':
    ket = 'Hari praktikum DDP'
elif praktikum == 'Rabu':
    ket = 'Hari praktikum Web'
elif praktikum == 'Jumat':
    ket = 'Hari praktikum front end'
else:
    ket = 'Hari kelas Literasi'

print(ket)