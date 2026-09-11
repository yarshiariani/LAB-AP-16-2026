# Data Penjualan
menu = ["Kopi Susu", "Matcha Latte", "Americano"]
harga = [18000, 22000, 15000]
jumlah = [4, 3, 5]

# 1. Menghitung subtotal
sub_kopi = harga[0] * jumlah[0]
sub_matcha = harga[1] * jumlah[1]
sub_americano = harga[2] * jumlah[2]
subtotal_pendapatan = [sub_kopi, sub_matcha, sub_americano]

# 2. Menghitung total dan pendapatan bersih
total_seluruh = sub_kopi + sub_matcha + sub_americano
BIAYA_OPERASIONAL = 15000
pendapatan_bersih = total_seluruh - BIAYA_OPERASIONAL

# 3. Menghitung jumlah barang terjual dan evaluasi target
total_barang = jumlah[0] + jumlah[1] + jumlah[2]
target_tercapai = total_seluruh > 200000 and total_barang > 10

# Menampilkan Hasil
print("Subtotal Pendapatan:", subtotal_pendapatan)
print("Pendapatan Bersih:", pendapatan_bersih)
print("Target Tercapai:", target_tercapai)