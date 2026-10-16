# Pemilihan Ketua Kelas "VoteClass"
def daftar_kandidat(kandidat_set, nama):
    nama_kapital = nama.capitalize()
    kandidat_set.add(nama_kapital)
    print(f"'{nama_kapital}' berhasil didaftarkan sebagai kandidat!\n")

def berikan_suara(rekap_suara, kandidat_set, nama_pemilih, pilihan):
    nama_pemilih_kecil = nama_pemilih.lower()
    pilihan_kapital = pilihan.capitalize()

    if pilihan_kapital not in kandidat_set:
        print(f"Error: Kandidat '{pilihan_kapital}' tidak terdaftar!\n")
    elif nama_pemilih_kecil in rekap_suara:
        print(f"'{nama_pemilih}' sudah memberikan suara sebelumnya!\n")
    else:
        rekap_suara[nama_pemilih_kecil] = pilihan_kapital
        print(f"Suara '{nama_pemilih}' untuk '{pilihan_kapital}' berhasil dicatat!\n")

def hitung_suara(rekap_suara, kandidat_set):
    perolehan = {}
    # Siapkan nilai 0 untuk semua kandidat
    for kandidat in kandidat_set:
        perolehan[kandidat] = 0
        
    # Tambah poin untuk tiap suara yang masuk
    for pilihan in rekap_suara.values():
        perolehan[pilihan] += 1
        
    return perolehan

def tampilkan_hasil(perolehan):
    print("\n=== HASIL PEMILIHAN KETUA KELAS ===")
    total_suara = sum(perolehan.values())
    
    suara_tertinggi = -1
    for suara in perolehan.values():
        if suara > suara_tertinggi:
            suara_tertinggi = suara

    pemenang = []
    for kandidat, suara in perolehan.items():
        print(f"{kandidat}: {suara} suara")
        if suara == suara_tertinggi:
            pemenang.append(kandidat)

    print("-" * 30)
    print(f"Total suara masuk: {total_suara}")
    
    if len(pemenang) > 1:
        nama_seri = ", ".join(pemenang)
        print(f"Hasil SERI antara: {nama_seri}")
        print("Perlu dilakukan pemilihan ulang!\n")
    else:
        print(f"PEMENANG: {pemenang[0]} dengan {suara_tertinggi} suara!\n")

# PROGRAM UTAMA
kandidat_tersedia = set() # Set = Kotak anti-duplikat
suara_masuk = {}          # Dictionary = Kotak pasangan (Pemilih : Pilihan)

print("=== SISTEM PEMILIHAN KETUA KELAS ===")
print("FASE PENDAFTARAN KANDIDAT")
while True:
    nama_calon = input("Masukkan nama kandidat (kosongkan untuk selesai): ")
    if nama_calon == "":
        if len(kandidat_tersedia) >= 2:
            break
        else:
            print("Minimal harus ada 2 kandidat untuk pemilihan!\n")
    else:
        daftar_kandidat(kandidat_tersedia, nama_calon)

print(f"Kandidat terdaftar: {kandidat_tersedia}\n")

print("FASE PEMUNGUTAN SUARA")
while True:
    pemilih = input("Nama pemilih (kosongkan untuk selesai): ")
    if pemilih == "":
        break
    
    print(f"Kandidat yang tersedia: {kandidat_tersedia}")
    pilihan_calon = input("Pilih kandidat: ")
    berikan_suara(suara_masuk, kandidat_tersedia, pemilih, pilihan_calon)

hasil_akhir = hitung_suara(suara_masuk, kandidat_tersedia)
tampilkan_hasil(hasil_akhir)
