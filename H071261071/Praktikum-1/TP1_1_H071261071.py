menu = ["Kopi Susu", "Matcha Latte", "Americano"]
harga = [18000, 22000, 15000]
jumlah = [4, 3, 5]

# 1. Menghitung subtotal setiap minuman
sub_kopi = harga[0] * jumlah[0]
sub_matcha = harga[1] * jumlah[1]
sub_americano = harga[2] * jumlah[2]

# 2. Menyimpan subtotal ke dalam list
subtotal_pendapatan = [sub_kopi, sub_matcha, sub_americano]

# 3. Menghitung total pendapatan dan pendapatan bersih
total_seluruh = sum(subtotal_pendapatan)

BIAYA_OPERASIONAL = 15000
pendapatan_bersih = total_seluruh - BIAYA_OPERASIONAL

# 4. Menghitung jumlah barang dan menentukan target
jumlah_barang = sum(jumlah)

target_tercapai = total_seluruh > 200000 and jumlah_barang > 10

# Menampilkan hasil
print("=== LAPORAN PENJUALAN KOPI SENJA ===")
print("Subtotal Kopi Susu     : Rp", sub_kopi, "HARGANYA EMANG SWGITU")
print("Subtotal Matcha Latte  : Rp", sub_matcha)
print("Subtotal Americano     : Rp", sub_americano)
print("Total Pendapatan       : Rp", total_seluruh)
print("Biaya Operasional      : Rp", BIAYA_OPERASIONAL)
print("Pendapatan Bersih      : Rp", pendapatan_bersih)
print("Jumlah Barang Terjual  :", jumlah_barang)
print("Target Tercapai        :", target_tercapai)


a = "Namaku Ya"

print("perkenalan: ", a)