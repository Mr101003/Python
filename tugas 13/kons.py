from MORE import*

class konsumen(MORE):
    nama = ''
    hari = ''
    beli = ''
    jumlah = 0
    harga = 0

    def __init__(self,kota, kecamatan, nama, hari, beli, jumlah, harga):
        super().__init__(kota, kecamatan)
        self.nama = nama
        self.hari = hari
        self.beli = beli
        self.jumlah = jumlah
        self.harga = harga

    def belanja(self):
        total = self.jumlah * self.harga
        print("=============================")
        super().lokasi()
        print(f"Nama        : {self.nama}")
        print(f"Hari        : {self.hari}")
        print(f"Beli        : {self.beli} x {self.jumlah}")
        print(f"Total       : {total}")
        print("=============================")

