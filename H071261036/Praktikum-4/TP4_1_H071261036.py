# Membuat fungsi untuk menghitung subtotal
def hitung_subtotal(harga, jumlah, adalah_member=False):
    subtotal = harga * jumlah
    if adalah_member:
        subtotal = subtotal - (subtotal * 0.10)
    return int(subtotal)

print("Selamat datang di Kasir Minimarket!")
status = input("Apakah Anda member? (y/n): ").lower()
is_member = True if status == 'y' else False

total_belanja = 0

while True:
    nama_barang = input("Masukkan nama barang (kosongkan untuk selesai): ")
    if nama_barang == "":
        break
    
    harga = int(input("Harga barang: "))
    jumlah = int(input("Jumlah barang: "))
    
    # Memanggil fungsi
    subtotal_barang = hitung_subtotal(harga, jumlah, is_member)
    print(f"Subtotal {nama_barang}: Rp{subtotal_barang}")
    
    total_belanja += subtotal_barang

print(f"Total belanja: Rp{total_belanja}")
