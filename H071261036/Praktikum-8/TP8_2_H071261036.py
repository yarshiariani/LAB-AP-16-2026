import re

def validasi_username(teks):
    # Diawali huruf, hanya boleh huruf/angka/garis bawah, total panjang 5-12
    pola = r"^[a-zA-Z][a-zA-Z0-9_]{4,11}$"
    return re.match(pola, teks)

print("\n=== Registrasi Username ===")
print("Ketik 'SELESAI' untuk mengakhiri.")

daftar_valid = [] 

while True: 
    uname = input("Masukkan username: ")
    if uname == "SELESAI":
        break
        
    if validasi_username(uname):
        print("Username tersedia.")
        daftar_valid.append(uname)
    else:
        print("Username tidak valid!")
        
print("\n=== Rekapitulasi ===")
print("Username valid:")

for i, u in enumerate(daftar_valid, 1):
    print(f"{i}. {u}")
print(f"Jumlah username valid: {len(daftar_valid)}")
