# fungsi (def)
# konsep sederhananya adalah kumpulan code yang bisa dipanggil dan digunakan berkali-kali (reusable)
# fungsi bisa menerima sebuah parameter

# sintaks fungsi
def nama_fungsi():
    print("Hello ini Fungsi")

# memanggil fungsi
nama_fungsi()

# contoh

def salam():
    print("Assalamualaikum")

salam()
salam()
salam()
salam()

# dengan paramater

salam("Ohayou gozaimasu")
salam("Konnichiwa")
salam("Konbanwa")

# contoh lain 
def luas_segitiga(alas,tinggi):
    luas = (alas * tinggi)/2
    print("Luas Segitiga : %i" %(luas))

luas_segitiga(4,7)
luas_segitiga(5,8)