d1 = {'nama':'rojulmen',
      'matkul':'pemweb'}

d2 = {'nama':'nasrul',
      'matkul':'ddp'}

d3 = {'nama':'misna',
      'matkul':'pti'}

d4 = {'nama':'fahmi',
      'matkul':'agama'}

data_dosen = [d1,d2,d3,d4]

for dosen in data_dosen:
    print('ini adalah data dari dosen',dosen['nama'])

    for d in dosen:
        print(d,dosen)