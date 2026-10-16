# Sistem Inventaris "BookNest"
# 1. MEMBUAT MESIN-MESIN KECIL (FUNGSI)
def tambah_buku(inventaris, judul, penulis, harga, stok):
    buku_baru = {"judul": judul, "penulis": penulis, "harga": harga, "stok": stok}
    inventaris.append(buku_baru)
    print(f"Buku '{judul}' berhasil ditambahkan!\n")

def cari_buku(inventaris, kata_kunci):
    ditemukan = []
    for buku in inventaris:
        if kata_kunci.lower() in buku["judul"].lower():
            ditemukan.append(buku)
            
    if len(ditemukan) > 0:
        print(f"Ditemukan {len(ditemukan)} buku:")
        for b in ditemukan:
            print(f"- {b['judul']} | {b['penulis']} | Rp{b['harga']} | Stok: {b['stok']}")
    else:
        print("Buku tidak ditemukan.\n")

def update_stok(inventaris, judul, jumlah):
    ketemu = False
    for buku in inventaris:
        if buku["judul"].lower() == judul.lower():
            ketemu = True
            if buku["stok"] + jumlah < 0:
                print("Gagal: Stok tidak boleh menjadi negatif!\n")
            else:
                buku["stok"] += jumlah
                print(f"Stok '{buku['judul']}' terupdate. Stok sekarang: {buku['stok']}\n")
            break
    if not ketemu:
        print("Error: Buku tidak ditemukan!\n")

def ringkasan_inventaris(inventaris):
    if len(inventaris) == 0:
        print("Inventaris masih kosong.\n")
        return

    total_stok = 0
    total_aset = 0
    buku_termahal = inventaris[0]

    for buku in inventaris:
        total_stok += buku["stok"]
        total_aset += (buku["harga"] * buku["stok"])
        if buku["harga"] > buku_termahal["harga"]:
            buku_termahal = buku

    print("=== RINGKASAN INVENTARIS BOOKNEST ===")
    print(f"Jumlah jenis buku: {len(inventaris)}")
    print(f"Total seluruh stok: {total_stok}")
    print(f"Total nilai aset : Rp{total_aset}")
    print(f"Buku termahal    : {buku_termahal['judul']} (Rp{buku_termahal['harga']})\n")

# 2. PROGRAM UTAMA (MESIN MENYALA TERUS)
inventaris_toko = [] # Laci utama masih kosong

print("=== SISTEM INVENTARIS TOKO BUKU BOOKNEST ===")
while True:
    print("Menu:\n1. Tambah Buku\n2. Cari Buku\n3. Update Stok\n4. Ringkasan Inventaris\n5. Keluar")
    pilihan = input("Pilih menu (1-5): ")

    if pilihan == '1':
        judul = input("Judul buku: ")
        penulis = input("Penulis: ")
        try:
            harga = int(input("Harga: "))
            stok = int(input("Stok awal: "))
            if harga < 0 or stok < 0:
                print("Harga dan stok tidak boleh negatif!\n")
            else:
                tambah_buku(inventaris_toko, judul, penulis, harga, stok)
        except ValueError:
            print("Error: Harga dan stok wajib diisi dengan ANGKA!\n")
            
    elif pilihan == '2':
        kunci = input("Masukkan kata kunci judul: ")
        cari_buku(inventaris_toko, kunci)
        
    elif pilihan == '3':
        judul_update = input("Judul buku yang ingin diupdate: ")
        try:
            ubah_stok = int(input("Jumlah perubahan (positif=tambah, negatif=kurang): "))
            update_stok(inventaris_toko, judul_update, ubah_stok)
        except ValueError:
            print("Error: Perubahan stok wajib ANGKA!\n")
            
    elif pilihan == '4':
        ringkasan_inventaris(inventaris_toko)
        
    elif pilihan == '5':
        print("Terima kasih telah menggunakan BookNest!")
        break
    else:
        print("Pilihan tidak valid.\n")
        
