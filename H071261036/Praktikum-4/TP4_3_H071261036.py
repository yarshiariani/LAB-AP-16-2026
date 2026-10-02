# Membuat fungsi rekursif
def hitung_mundur(angka):
    print(angka)
    if angka == 0:
        print("Luncurkan!")
    else:
        # Fungsi memanggil dirinya sendiri
        hitung_mundur(angka - 1)

while True:
    angka_awal = int(input("Masukkan angka awal hitung mundur: "))
    if angka_awal < 0:
        print("Input tidak valid, angka tidak boleh negatif.")
    else:
        hitung_mundur(angka_awal)
        break
    