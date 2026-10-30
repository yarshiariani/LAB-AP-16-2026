import re 

print("=== Validasi Data Mahasiswa ===")
nim = input("Masukkan NIM        : ")
email = input("Masukkan Email      : ")
telp = input("Masukkan No. Telp   : ")

# 1. RUMUS REGEX (POLA)
# Pola NIM: Diawali H071, diikuti 6 angka.
pola_nim = r"^H071\d{6}$" 

# Pola Email: huruf/angka, tanda @, huruf/angka, tanda titik, huruf/angka.
pola_email = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

# Pola Telp: Cuma berisi 10 sampai 13 angka.
pola_telp = r"^\d{10,13}$"

# 2. PROSES PENGECEKAN (Menggunakan re.match)
cek_nim = re.match(pola_nim, nim)
cek_email = re.match(pola_email, email)
cek_telp = re.match(pola_telp, telp)

# 3. CETAK HASIL
print("\n--- Hasil Validasi ---")

if cek_nim:
    print("NIM         : Valid")
else:
    print("NIM         : Format NIM tidak valid!")
    
if cek_email:
    print("Email       : Valid")
else:
    print("Email       : Format email tidak valid!")
    
if cek_telp:
    print("No. Telepon : Valid")
else:
    print("No. Telepon : Nomor telepon tidak valid!")

if cek_nim and cek_email and cek_telp:
    print("\nData mahasiswa berhasil diverifikasi!")
