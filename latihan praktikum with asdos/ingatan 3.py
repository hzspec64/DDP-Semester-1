# jika ipk nya 3.71 sampai 4.00, maka masuk kat. cumlaude
# jika ipk nya 3.31 sampai 3.70, maka masuk kat. sangat memuaskan
# jika ipk nya 2.81 sampai 3.30, maka masuk kat. memuaskan
# selain itu adalah kategori cukup

ipk = 3.88

if 4.00 >= ipk >= 3.71:
    kat = 'Cumlaude'
elif ipk >= 3.31 and ipk <= 3.70:
    kat = 'Sangat Memuaskan'
elif ipk >= 2.81 and ipk <= 3.30:
    kat = 'Memuaskan'
else:
    ket = 'Cukup'

print(kat)