class MORE:
    kota = ''
    kecamatan = ''
    
    def __init__(self, kota, kecamatan):
        self.kota = kota
        self.kecamatan = kecamatan

    def lokasi(self):
        print(f"lokasi      : kota {self.kota}, Kecamatan {self.kecamatan}")


