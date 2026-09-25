# Meminta input kursi bus yang valid
while True:
    try:
        maks_kursi = int(input("Masukkan maksimal kursi bus: "))
        break
    except ValueError:
        print("Input jumlah kursi harus berupa angka!")

print("\nSistem Reservasi PO BUS Dimulai")
sisa_kursi = maks_kursi
total_pendapatan = 0

while sisa_kursi > 0:
    print(f"Sisa kursi: {sisa_kursi}")
    try:
        umur = int(input("Masukkan umur penumpang: "))
        
        if umur < 0:
            print("Umur tidak valid!")
            continue
            
        elif umur <= 5:
            kategori = "Balita"
            harga = 0
            print("Kategori: Balita")
            print("Tiket Gratis (Rp 0)")
        elif umur <= 12:
            kategori = "Anak"
            harga = 50000
            print("Kategori: Anak Harga: Rp 50.000")
        else:
            kategori = "Dewasa"
            harga = 100000
            print("Kategori: Dewasa Harga: Rp 100.000")
            
        sisa_kursi -= 1
        total_pendapatan += harga
        
    except ValueError:
        print("Input umur harus berupa angka!")

print("Semua Kursi Terisi")
print(f"Total pendapatan perjalanan PO BUS kali ini: Rp {total_pendapatan}")
