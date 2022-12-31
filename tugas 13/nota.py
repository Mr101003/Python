from staff import*
from stok import*
from kons import*

staf = STAFF("Depok", "Beji", "Rafly", "Rabu")
barang = STOK("Depok", "Beji", "munchies soju grape Liquid", 100, 130000)
customer = konsumen("Depok", "Beji", "Farid", "Rabu", "munchies soju grape Liquid", 2, 130000)


staf.jam_masuk()
barang.jumlah_barang()
customer.belanja()
barang.pembelian()
barang.jumlah_barang()