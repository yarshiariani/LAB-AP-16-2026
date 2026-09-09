#Tugas Praktikum
#Pertemuan 1- Tugas 1
menu = ["Kopi Susu", "Matcha Latte", "Americano"]
harga = [18000, 22000, 15000]
jumlah = [4, 3, 5]

#Subtotal untuk Kopi Susu, Matcha Latte, dan Americano berdasarkan data dan harga
sub_kopi = harga[0]*jumlah[0]
sub_matcha = harga [1]*jumlah[1]
sub_americano = harga [2]*jumlah[2]

#Menyatukan ketiga subtotal dalam satu list
subtotal_pendapatan = [sub_kopi, sub_matcha, sub_americano]

#Menghitung total_seluruh dan pendapatan bersih
BIAYA_OPERASIONAL = 15000
total_seluruh = sub_kopi+sub_matcha+sub_americano
pendapatan_bersih = total_seluruh-BIAYA_OPERASIONAL

#Menghitung jumlah barang yang terjual dan target tercapai
jumlah_barang_terjual = jumlah[0]+jumlah[1]+jumlah[2]
target_tercapai = total_seluruh > 200000 and jumlah_barang_terjual > 10

print (subtotal_pendapatan)
print (pendapatan_bersih)
print (target_tercapai)
