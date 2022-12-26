class Gempa:
    lokasi = ''
    Skala = 0
    def __init__(self, lokasi, skala):
        self.lokasi = lokasi
        self.skala = skala

    def dampak(self):
        if self.skala < 2:
            print("=================================")
            print(f"lokasi : {self.lokasi}")
            print(f"skala  : {self.skala}")
            print("dampak   : Gempa tidak terasa")
            print("=================================")

        elif self.skala >= 2 and self.skala < 4:
            print("=================================")
            print(f"lokasi : {self.lokasi}")
            print(f"skala  : {self.skala}")
            print("dampak   : Bangunan Retak-retak")
            print("=================================")

        elif self.skala >= 4 and self.skala < 6:
            print("=================================")
            print(f"lokasi : {self.lokasi}")
            print(f"skala  : {self.skala}")
            print("dampak   : Bangunan Roboh")
            print("=================================")

        else :
            print("=================================")
            print(f"lokasi : {self.lokasi}")
            print(f"skala  : {self.skala}")
            print("dampak   : Bangunan Roboh dan Berpotensi Tsunami")
            print("=================================")