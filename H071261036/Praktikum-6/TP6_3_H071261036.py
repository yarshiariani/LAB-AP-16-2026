# Playlist Musik "PlayTune"
def tambah_lagu(playlist, genre_set, judul, artis, genre, durasi):
    # Tuple ditandai dengan kurung biasa ()
    lagu_baru = (judul, artis, genre, durasi)
    playlist.append(lagu_baru)
    genre_set.add(genre)
    print(f"Lagu '{judul}' oleh {artis} berhasil ditambahkan!\n")

def tampilkan_playlist(playlist):
    if len(playlist) == 0:
        print("Playlist kosong.\n")
        return

    print("No | Judul | Artis | Genre | Durasi")
    print("-" * 40)
    
    total_detik_semua = 0
    # enumerate itu alat bantu hitung otomatis (mulai dari angka 1)
    for index, lagu in enumerate(playlist, start=1):
        judul, artis, genre, durasi = lagu
        menit = durasi // 60
        detik = durasi % 60
        total_detik_semua += durasi
        
        # :02d itu agar detik 5 ditulis jadi 05 (dua digit)
        print(f"{index}. {judul} | {artis} | {genre} | {menit}:{detik:02d}")
        
    total_menit = total_detik_semua // 60
    sisa_detik = total_detik_semua % 60
    print("-" * 40)
    print(f"Total durasi playlist: {total_menit} menit {sisa_detik} detik\n")

def filter_genre(playlist, genre_target):
    # Ini namanya List Comprehension (rumus satu baris pengganti perulangan for)
    hasil = [lagu for lagu in playlist if lagu[2].lower() == genre_target.lower()]
    return hasil

def hapus_lagu(playlist, nomor):
    # Karena urutan komputer mulai dari 0, tapi user ngetik urutan 1, maka dikurang 1
    indeks_asli = nomor - 1
    if 0 <= indeks_asli < len(playlist):
        lagu_dihapus = playlist.pop(indeks_asli)
        print(f"Lagu '{lagu_dihapus[0]}' berhasil dihapus!\n")
    else:
        print("Nomor lagu tidak valid.\n")

def statistik_playlist(playlist, genre_set):
    if len(playlist) == 0:
        print("Playlist kosong, tidak ada statistik.\n")
        return

    print("=== STATISTIK PLAYLIST PLAYTUNE ===")
    print(f"Total lagu   : {len(playlist)}")
    print(f"Jumlah genre : {len(genre_set)}")
    print(f"Daftar genre : {genre_set}")
    
    print("Distribusi genre:")
    distribusi = {}
    # Menghitung lagu pakai dictionary
    for lagu in playlist:
        genre_lagu = lagu[2]
        if genre_lagu in distribusi:
            distribusi[genre_lagu] += 1
        else:
            distribusi[genre_lagu] = 1
            
    for g, jumlah in distribusi.items():
        print(f"- {g}: {jumlah}")

    # Mencari yang terpanjang dan terpendek
    lagu_panjang = playlist[0]
    lagu_pendek = playlist[0]

    for lagu in playlist:
        if lagu[3] > lagu_panjang[3]:
            lagu_panjang = lagu
        if lagu[3] < lagu_pendek[3]:
            lagu_pendek = lagu

    m_panjang = lagu_panjang[3] // 60
    d_panjang = lagu_panjang[3] % 60
    m_pendek = lagu_pendek[3] // 60
    d_pendek = lagu_pendek[3] % 60

    print(f"Lagu terpanjang: {lagu_panjang[0]} ({m_panjang}:{d_panjang:02d})")
    print(f"Lagu terpendek : {lagu_pendek[0]} ({m_pendek}:{d_pendek:02d})\n")

# PROGRAM UTAMA
daftar_playlist = []
kumpulan_genre = set()

print("=== PLAYLIST MUSIK PLAYTUNE ===")
while True:
    print("Menu:\n1. Tambah Lagu\n2. Tampilkan Playlist\n3. Filter Genre\n4. Hapus Lagu\n5. Statistik\n6. Keluar")
    pilih = input("Pilih menu (1-6): ")

    if pilih == '1':
        judul_lagu = input("Judul lagu: ")
        artis_lagu = input("Artis: ")
        genre_lagu = input("Genre: ")
        try:
            durasi_lagu = int(input("Durasi (dalam detik): "))
            if durasi_lagu < 0:
                print("Durasi tidak boleh negatif!\n")
            else:
                tambah_lagu(daftar_playlist, kumpulan_genre, judul_lagu, artis_lagu, genre_lagu, durasi_lagu)
        except ValueError:
            print("Durasi wajib ANGKA!\n")
            
    elif pilih == '2':
        tampilkan_playlist(daftar_playlist)
        
    elif pilih == '3':
        print(f"Genre tersedia: {kumpulan_genre}")
        g_cari = input("Masukkan genre yang ingin difilter: ")
        hasil_filter = filter_genre(daftar_playlist, g_cari)
        print(f"Lagu bergenre '{g_cari}':")
        for i, lagu in enumerate(hasil_filter, 1):
            m = lagu[3] // 60
            d = lagu[3] % 60
            print(f"{i}. {lagu[0]} oleh {lagu[1]} ({m}:{d:02d})")
        print()
            
    elif pilih == '4':
        tampilkan_playlist(daftar_playlist)
        if len(daftar_playlist) > 0:
            try:
                nomor_hapus = int(input("Masukkan nomor lagu yang mau dihapus: "))
                hapus_lagu(daftar_playlist, nomor_hapus)
            except ValueError:
                print("Masukkan urutan pakai ANGKA!\n")
                
    elif pilih == '5':
        statistik_playlist(daftar_playlist, kumpulan_genre)
        
    elif pilih == '6':
        print("Terima kasih telah menggunakan PlayTune!")
        break
    