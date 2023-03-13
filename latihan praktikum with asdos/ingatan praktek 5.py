p1 = {'Nama':'Naruto',
      'Asal':'Jakarta',
      'Program':'Beastudi'}

p2 = {'Nama':'Sasuke',
      'Asal':'Bogor',
      'Program':'Beastudi'}

p3 = {'Nama':'Sakura',
      'Asal':'Depok',
      'Program':'Beastudi'}

p4 = {'Nama':'Sai',
      'Asal':'Jakarta',
      'Program':'Reguler'}

data_mahasiswa = [p1,p2,p3,p4]
#print(data_diri)

for mahasiswa in data_mahasiswa:
    print('-----------------')
    print('Ini adalah data mahasiswa',mahasiswa['Nama'])

    for key in mahasiswa:
        print(key,':',mahasiswa[key])