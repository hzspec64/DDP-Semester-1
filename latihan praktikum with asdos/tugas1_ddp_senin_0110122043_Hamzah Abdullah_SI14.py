# ----List Data Karyawan----
p1 = {'Nama':'Budi','Jabatan':'Manager','Agama':'Islam','Status':'Menikah'}
p2 = {'Nama':'Siti','Jabatan':'Asisten Manager','Agama':'Islam','Status':'Menikah'}
p3 = {'Nama':'I Gede','Jabatan':'Supervisor','Agama':'Hindu','Status':'Menikah'}
p4 = {'Nama':'Joko','Jabatan':'Staff','Agama':'Islam','Status':'Belum Menikah'}
p5 = {'Nama':'Alex','Jabatan':'Staff','Agama':'Kristen Protestan','Status':'Belum Menikah'}
ar_pegawai = [p1,p2,p3,p4,p5]

print('\n-----List Data Karyawan PT. Howyoverse Tbk-----')
for pegawai in ar_pegawai:
    for key, data in pegawai.items():
        print(key,':',data)
# ----Gaji Pokok Karyawan----
        gj = pegawai['Jabatan']
        if gj == 'Manager':
            gkok = 15000000
        elif gj == 'Asisten Manager':
            gkok = 10000000
        elif gj == 'Supervisor':
            gkok = 7000000
        else:
            gkok = 4000000

# ----Gaji & Pengeluaran Lain Karyawan----
        tj_jb = 0.3 * gkok
        bpjs = 0.10 * gkok
        tj_kl = pegawai['Status']
        ket = (0,gkok * 0.10)[tj_kl == 'Menikah']
        ga_to = gkok + tj_jb + bpjs + ket
        zapo = pegawai['Agama'] 
        zapo = (0, 0.025 * ga_to)[ga_to >= 7000000 and zapo == 'Islam']
        gabe = ga_to - zapo
    print('Gaji Pokok \t\t: Rp.',gkok,
      '\nTunjangan Jabatan \t: Rp.',tj_jb,
      '\nBPJS \t\t\t: Rp.',bpjs,
      '\nTunjangan Keluarga \t: Rp.',ket,
      '\nGaji Kotor \t\t: Rp.',ga_to,
      '\nZakat Profesi \t\t: Rp.',zapo,
      '\nGaji Bersih \t\t: Rp.',gabe,         
      '\n-----------------------------------------')   