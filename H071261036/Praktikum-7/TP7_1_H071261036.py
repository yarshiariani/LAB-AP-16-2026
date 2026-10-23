import os
import random
from datetime import datetime

# Membuat folder 'invoices' 
if not os.path.exists("invoices"):
    os.makedirs("invoices")

def buat_transaksi():
    print("\n=== 1. TRANSAKSI BARU ===")
    nama_kasir = input("Masukkan nama kasir: ")
    
    daftar_belanja = []
    total_harga = 0
    
    # Looping untuk memasukkan banyak barang belanjaan
    while True:
        nama_produk = input("Nama produk (kosongkan & tekan Enter jika selesai): ")
        if nama_produk == "":
            break
            
        harga_produk = int(input(f"Harga {nama_produk}: "))
        jumlah_produk = int(input(f"Jumlah {nama_produk}: "))
        
        subtotal = harga_produk * jumlah_produk
        total_harga = total_harga + subtotal
        
        # Simpan barang ke dalam laci (List)
        daftar_belanja.append( (nama_produk, harga_produk, jumlah_produk, subtotal) )
        
    if len(daftar_belanja) == 0:
        print("Transaksi dibatalkan, tidak ada barang.")
        return

    # --- PROSES PEMBUATAN ID INVOICE ---
    inisial = nama_kasir[:3].upper()
    waktu_sekarang = datetime.now()
    
    tahun = waktu_sekarang.strftime("%y")
    bulan = waktu_sekarang.strftime("%m")
    tanggal = waktu_sekarang.strftime("%d")
    jam_menit = waktu_sekarang.strftime("%H%M")
    angka_acak = random.randint(100, 999)
    
    # Gabungkan semua jadi ID Transaksi (Contoh: YAR2610231102999)
    id_transaksi = f"{inisial}{tahun}{bulan}{tanggal}{jam_menit}{angka_acak}"
    nama_file_invoice = f"invoices/{id_transaksi}.txt"
    
    # --- SOAL 1: MENULIS STRUK KE DALAM FILE (MODE "w") ---
    with open(nama_file_invoice, "w") as file_invoice:
        file_invoice.write("==============================\n")
        file_invoice.write("         STRUK BELANJA        \n")
        file_invoice.write("==============================\n")
        file_invoice.write(f"ID Trx : {id_transaksi}\n")
        file_invoice.write(f"Kasir  : {nama_kasir}\n")
        file_invoice.write("------------------------------\n")
        
        for barang in daftar_belanja:
            nama = barang[0]
            harga = barang[1]
            jumlah = barang[2]
            sub = barang[3]
            file_invoice.write(f"{nama}\n")
            file_invoice.write(f"   {jumlah} x Rp{harga} = Rp{sub}\n")
            
        file_invoice.write("------------------------------\n")
        file_invoice.write(f"TOTAL: Rp{total_harga}\n")
        file_invoice.write("==============================\n")
        
    print(f"\nBerhasil! Invoice disimpan dengan nama: {id_transaksi}.txt")
    
    # --- SOAL 3: MENCATAT RIWAYAT TRANSAKSI (MODE "a") ---
    nama_file_riwayat = "trx_history.txt"
    waktu_lengkap = waktu_sekarang.strftime("%Y-%m-%d %H:%M:%S")
    
    # Jika file riwayat belum ada, buatkan atap/header tabelnya dulu
    if not os.path.exists(nama_file_riwayat):
        with open(nama_file_riwayat, "w") as file_riwayat:
            file_riwayat.write("===================================================================\n")
            file_riwayat.write("| Waktu               | ID Transaksi         | Nominal Transaksi  |\n")
            file_riwayat.write("===================================================================\n")
            
    # Mode "a" (Append) agar transaksi baru ditambahkan di baris paling bawah, bukan menghapus yang lama
    with open(nama_file_riwayat, "a") as file_riwayat:
        teks_baris = f"| {waktu_lengkap} | {id_transaksi}     | Rp. {total_harga}          |\n"
        file_riwayat.write(teks_baris)
        file_riwayat.write("-------------------------------------------------------------------\n")


def cari_invoice():
    print("\n=== 2. CARI INVOICE ===")
    id_cari = input("Masukkan ID Transaksi (tanpa .txt): ")
    nama_file = f"invoices/{id_cari}.txt"
    
    # --- SOAL 2: MEMBACA FILE INVOICE (MODE "r") ---
    try:
        # Mode "r" (Read) hanya untuk membaca isi file
        with open(nama_file, "r") as file_invoice:
            isi_teks = file_invoice.read()
            print("\nIsi Invoice:")
            print(isi_teks)
    except FileNotFoundError:
        print(f"Maaf, invoice dengan ID '{id_cari}' tidak ditemukan.")


# --- MENU UTAMA APLIKASI ---
while True:
    print("\n=== APLIKASI KASIR ===")
    print("1. Transaksi Baru")
    print("2. Cari Invoice")
    print("3. Keluar")
    pilihan = input("Pilih menu (1-3): ")
    
    if pilihan == "1":
        buat_transaksi()
    elif pilihan == "2":
        cari_invoice()
    elif pilihan == "3":
        print("Terima kasih, program ditutup.")
        break
    else:
        print("Pilihan salah!")
        