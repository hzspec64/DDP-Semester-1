# jika tinggi badan lebih dari 186, maka masuk kat. jangkung
# jika tinggi badan 175 sampai 185, maka masuk kat. hansamu
# jika tinggi badan 165 sampai 174, maka masuk kat. standar
# selain itu adalah daus mini

tinggi_badan = 182

if tinggi_badan >= 186:
    kat = 'Jangkung'
elif tinggi_badan >= 175 and tinggi_badan <= 185:
    kat = 'Hansamu'
elif tinggi_badan >= 165 and tinggi_badan <= 174:
    kat = 'Standar'
else:
    kat = 'Daus Mini'

print(kat)