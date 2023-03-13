class Person:
    # variabel kosong nama, gender, dan umur
    nama = ""
    gender = ""
    umur = 0

    # membuat attribute (identitas) atau fungsi constructor
    def __init__(self,nama,gender,umur):
        self.nama = nama
        self.gender = gender
        self.umur = umur

    # membuat method cetak
    def cetak(self):
        print("Nama\t\t :",self.nama,
              "\nGender\t\t :",self.gender,
              "\nUmur\t\t :",self.umur,
            )