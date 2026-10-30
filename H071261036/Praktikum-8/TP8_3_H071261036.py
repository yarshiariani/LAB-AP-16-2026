import re

print("\n=== Pembersihan Data Nomor Telepon ===")
jumlah = int(input("Masukkan jumlah data: "))

# Tampung input kotor ke dalam List sementara
data_awal = []
for i in range(1, jumlah + 1):
    no = input(f"Nomor ke-{i}: ")
    data_awal.append(no)
    
print("\n--- Hasil Pembersihan ---")
valid_count = 0

for i, no_kotor in enumerate(data_awal, 1):
    # 1. MENGHAPUS SPASI DAN STRIP 
    no_bersih = re.sub(r"[\s-]", "", no_kotor)
    
    # 2. CEK NOMOR
    is_valid = re.match(r"^\d{10,13}$", no_bersih)
    
    print(f"Data {i}:")
    print(f"Sebelum: {no_kotor}")
    print(f"Sesudah: {no_bersih}")
    
    if is_valid:
        print("Status : Valid\n")
        valid_count += 1
    else:
        print("Status : Tidak valid\n")
        
print(f"Jumlah nomor valid: {valid_count}")
