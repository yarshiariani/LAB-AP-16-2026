"Laporan Penjualan Kopi Senja"

menu = ["Kopi Susu", "Matcha Latte", "Americano"]
harga = [18000, 22000, 15000]
jumlah = [4, 3, 5]

sub_kopi = harga[0] * jumlah[0]     
sub_matcha = harga[1] * jumlah[1]      
sub_americano = harga[2] * jumlah[2]  

subtotal_pendapatan = [sub_kopi, sub_matcha, sub_americano]

total_seluruh = sum(subtotal_pendapatan)
BIAYA_OPERASIONAL = 15000
pendapatan_bersih = total_seluruh - BIAYA_OPERASIONAL

jumlah_terjual = sum(jumlah)
target_tercapai = total_seluruh > 200000 and jumlah_terjual > 10

# print(f"Subtotal {menu[0]}: Rp{sub_kopi:,}")
# print(f"Subtotal {menu[1]}: Rp{sub_matcha:,}")
# print(f"Subtotal {menu[2]}: Rp{sub_americano:,}")
# print("------------------------------------")
# print(f"Total Pendapatan Kotor : Rp{total_seluruh:,}")
# print(f"Pendapatan Bersih      : Rp{pendapatan_bersih:,}")
# print("------------------------------------")
# print(f"Jumlah Barang Terjual  : {jumlah_terjual}")
# print(f"Target Tercapai        : {target_tercapai}")


print("subtotal kopi susu: Rp",sub_kopi)
print("total pendapatan kotor: Rp",total_seluruh)
print("target tercapai: ",target_tercapai)

a = "Namaku Fadel"

print("Perkenalan: ", a)
