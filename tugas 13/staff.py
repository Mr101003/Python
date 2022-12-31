from MORE import*

class STAFF(MORE):
    Nama = ''
    Shift = ''

    def __init__(self,kota, kecamatan, nama, shift):
        super().__init__(kota, kecamatan)
        self.Nama = nama
        self.Shift = shift

    def jam_masuk(self):
        print("=============================")
        super().lokasi()
        print(f"Nama Staff  : {self.Nama}")
        print(f"Hari        : {self.Shift}")
        print("=============================")




