data_nilai = {'Echidna':75, 'Asta':98, 'Levi':59,
              'Loid':100, 'Enterprise':88, 'Luffy':45}
data_nilai['Echidna'] = 80 #ubah data
data_nilai.pop('Asta')
del data_nilai['Luffy']

# cetak all
print('Data Nilai',data_nilai)

# cetak nilai (value)nya saja
for nilai in data_nilai.values():
    print('Daftar Nilai:',nilai)

# cetak key (index)nya saja
for nama in data_nilai.keys():
    print('Daftar Siswa:',nama)

# cetak all manual
for nama,nilai in data_nilai.items():
    ket = ('Lulus','Gagal')[nilai < 60]
    print('Daftar Siswa:',nama,
          'Nilai:',nilai,
          'Dinyatakan:',ket)