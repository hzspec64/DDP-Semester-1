class Bank:
#member1 variabel
    norek = ''
    nama = ''
    saldo = 0
    jmlNasabah = 0 # variabel static
    BANK = 'Bank Syariah Nurul Fikri' # variabel konstanta

#member2 konstruktor
def __init__(self,no,nasabah,saldo):
    self.norek = no
    self.nama = nasabah
    self.saldo = saldo
    Bank.jmlNasabah += 1
