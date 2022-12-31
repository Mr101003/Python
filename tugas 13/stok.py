from MORE import*

class STOK(MORE):
    barang = ''
    harga = 0
    jumlah = 0

    def __init__(self, kota, kecamatan, barang, jumlah, harga):
        super().__init__(kota, kecamatan)
        self.barang = barang
        self.harga = harga
        self.jumlah = jumlah

    
    def jumlah_barang(self):
        print("=============================")
        super().lokasi()
        print(f"Barang      : {self.barang}")
        print(f"Jumlah Stok : {self.jumlah}")
        print("=============================")

    def pembelian(self):
        self.jumlah -= 1


