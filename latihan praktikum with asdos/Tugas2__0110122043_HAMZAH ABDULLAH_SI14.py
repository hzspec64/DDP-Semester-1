# ----List Data Karyawan PT. Howyoverse Tbk----
p1 = {'Nama':'Budi','Jabatan':'Manager','Agama':'Islam','Status':'Menikah'}
p2 = {'Nama':'Siti','Jabatan':'Asisten Manager','Agama':'Islam','Status':'Menikah'}
p3 = {'Nama':'I Gede','Jabatan':'Supervisor','Agama':'Hindu','Status':'Menikah'}
p4 = {'Nama':'Joko','Jabatan':'Staff','Agama':'Islam','Status':'Belum Menikah'}
p5 = {'Nama':'Alex','Jabatan':'Staff','Agama':'Kristen Protestan','Status':'Belum Menikah'}
ar_pegawai = [p1,p2,p3,p4,p5]

# ----Input Output Data Gaji Karyawan----
print("-------Cari Data Gaji Karyawan PT. Howyoverse Tbk-------")

nm = str(input('Masukkan Nama\t: '))
jb = str(input('Masukkan Jabatan: '))
ag = str(input('Masukkan Agama\t: '))
st = str(input('Masukkan Status\t: '))

print('\nNama\t\t\t:',nm,
      '\nJabatan\t\t\t:',jb,
      '\nAgama\t\t\t:',ag,
      '\nStatus\t\t\t:',st)

if jb == 'Manager':
  gpo = 15000000
elif jb == 'Asisten Manager':
  gpo = 10000000
elif jb == 'Supervisor':
  gpo = 7000000
else:
  gpo = 4000000
print('Gaji Pokok\t\t: Rp.',gpo)

tb = 0.30 * gpo
sjbp = 0.10 * gpo
if st == 'Menikah':
  tk = 0.1 * gpo
else :
  tk = 0

gko = gpo + tb + sjbp

zp = (0,0.025 * gko)[gko >= 7000000 and ag == 'Islam']

gb = gko - zp

print('BPJS\t\t\t: Rp.',sjbp)
print('Tunjangan Keluarga\t: Rp.',tk)
print('Gaji Kotor\t\t: Rp.',gko)
print('Zakat Profesi\t\t: Rp.',zp)
print('Gaji Bersih\t\t: Rp.',gb)