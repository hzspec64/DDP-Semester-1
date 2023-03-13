p1 = {'nama':'Budi','jabatan':'manager','agama':'islam','status':'menikah'}
p2 = {'nama':'Siti','jabatan':'asisten manager','agama':'islam','status':'menikah'}
p3 = {'nama':'I Gede','jabatan':'supervisor','agama':'hindu','status':'menikah'}
p4 = {'nama':'Joko','jabatan':'staff','agama':'islam','status':'belum menikah'}
p5 = {'nama':'Alex','jabatan':'staff','agama':'kristen protestan','status':'belum menikah'}

ar_pegawai = [p1, p2, p3, p4, p5]
for pegawai in ar_pegawai:
    for key, data in pegawai.items():
        #mencari gapok pegawai
        gaji = pegawai['jabatan']
        if gaji == 'manager':
            gapok = 15000000
        elif gaji == 'asisten manager':
            gapok = 10000000
        elif gaji == 'supervisor':
            gapok = 7000000
        else:
            gapok = 4000000
    # mencari elemen gaji lain
        tunjangan_jabatan = 0.3 * gapok
        bpjs = 0.10 * gapok
        tunjangan_keluarga = pegawai['status']
        ket = (0,gapok * 0.10)[tunjangan_keluarga == 'menikah']
        gaji_kotor = gapok + tunjangan_jabatan + bpjs + ket
        zakprof = pegawai['agama'] 
        zakat_profesi = (0, 0.025 * gaji_kotor)[gaji_kotor >= 7000000 and zakprof == 'islam']
        gaji_bersih = gaji_kotor - zakat_profesi
        print(key,':',data)
    print('gaji pokok \t\t:',gapok,
            '\ntunjangan jabatan \t:',tunjangan_jabatan,
            '\nBPJS \t\t\t:',bpjs,
            '\ntunjangan keluarga \t:',ket,
            '\ngaji kotor \t\t:',gaji_kotor,
            '\nzakat profesi \t\t:',zakat_profesi,
            '\ngaji bersih \t\t:',gaji_bersih,         
            '\n----------------------')   