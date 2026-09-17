jarak = float(input("Masukkan jarak pengiriman (km): "))
express = input("Layanan express (ya/tidak): ").lower()

# Menentukan tarif dasar pakai conditional biasa
if jarak < 5:
    tarif_dasar = 10000
elif jarak <= 20:
    tarif_dasar = 20000
else:
    tarif_dasar = 35000

# Menentukan biaya tambahan pakai Ternary Operator
biaya_tambahan = 15000 if express == "ya" else 0

total = tarif_dasar + biaya_tambahan
print(f"Total tarif pengiriman: Rp{total}")
