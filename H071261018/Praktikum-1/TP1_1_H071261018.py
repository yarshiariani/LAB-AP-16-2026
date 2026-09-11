# Data Penjualan
menu = ["Kopi Susu", "Matcha Latte", "Americano"]
harga = [18000, 22000, 15000]
jumlah = [4, 3, 5,]

#Subtotal masing-masing minuman
sub_kopi = harga[0] * jumlah[0]
sub_matcha = harga[1] * jumlah[1]
sub_americano = harga[2] * jumlah[2]

#Memasukkan ke dalam List
subtotal_pendapatan = [sub_kopi, sub_matcha, sub_americano]

#Total seluruh & pendapatan bersih
BIAYA_OPERASIONAL = 15000
total_seluruh = sum(subtotal_pendapatan)
pendapatan_bersih = total_seluruh - BIAYA_OPERASIONAL

#Jumlah barang  terjual & cek target
jumlah_barang = sum(jumlah)
target_tercapai = total_seluruh > 200000 and jumlah_barang > 10

#Menampilkan hasilnya
print("Subtotal Kopi Susu      :", sub_kopi)
print("Subtotal Matcha Latte   :", sub_matcha)
print("Subtotal Americano      :", sub_americano)
print("List subtotal_pendapatan :", subtotal_pendapatan)
print("Total Pendapatan        :", total_seluruh)
print("Pendapatan Bersih       :", pendapatan_bersih)
print("Jumlah Barang Terjual   :", jumlah_barang)
print("Target Tercapai         :", target_tercapai)



