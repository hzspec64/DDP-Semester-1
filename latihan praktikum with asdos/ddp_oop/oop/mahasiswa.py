from person import *

class Mahasiswa(Person):
    # variabel kosong prodi, semester
    prodi = ""
    semester = 0

    # membuat attribute yang diambil dari parent class
    def __init__(self,nama,gender,umur,prodi,semester):
        super().__init__(nama,gender,umur)
        self.prodi = prodi
        self.semester = semester

    # method cetak
    def cetak(self):
        super().cetak()
        print("Prodi\t\t :",self.prodi,
              "\nSemester\t :",self.semester,
            )