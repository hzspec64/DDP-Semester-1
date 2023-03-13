class Bank:
    # variabel member
    norek = ""
    nama = ""
    saldo = 0
    jmlNasabah = 0 # variabel static
    BANK = "Bank Syariah Nurul Fikri" # variabel konstanta

    # fungsi attribute (identitas) atau fungsi constructor
    def __init__(self, no, nasabah, uang):
        self.norek = no
        self.nama = nasabah
        self.saldo = uang
        Bank.jmlNasabah += 1
    
    # membuat method
    def nabung(self, uang):
        # self.saldo = self.saldo + uang
        self.saldo += uang
    
    def tarik(self, uang):
        # self.saldo = self.saldo - uang
        self.saldo -= uang
    
    def cetak(self):
        print(Bank.BANK,
            "\n-----------------------------------------",
            "\nNo. Rekening\t:", self.norek,
            "\nNama Nasabah\t:", self.nama,
            "\nSaldo\t\t: Rp. ", format(self.saldo, ","),
            "\n========================================="
        )