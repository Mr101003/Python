# Mu'adz - TI02
# Tugas DDP 12
from gempa import*

#input data
GempaPertama = Gempa('banten', 1.2)
GempaKedua = Gempa('palu', 6.1)
GempaKetiga = Gempa('Cianjur', 5.6)
GempaKeempat = Gempa('Jayapura', 3.3)
GempaKelima = Gempa('Garut', 4.0)


# hasil data dampak
GempaPertama.dampak()
GempaKedua.dampak()
GempaKetiga.dampak()
GempaKeempat.dampak()
GempaKelima.dampak()