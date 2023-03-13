# jika nilai anda adalah 91 ke atas, maka mendapatkan grade A
# jika nilai anda adalah 78 sampai 90, maka mendapatkan grade B
# jika nilai anda adalah 61 sampai 77, maka mendapatkan grade C
# jika nilai anda adalah 40 sampai 60, maka mendapatkan grade D
# selain itu anda mendapatkan grade F

nilai = 85

if 91 >= nilai:
    grade = 'Grade A'
elif nilai >= 78 and nilai <= 90:
    grade = 'Grade B'
elif nilai >= 61 and nilai <= 77:
    grade = 'Grade C'
elif nilai >= 40 and nilai <= 60:
    grade = 'Grade D'
else:
    grade = 'Grade F'

print(grade)