# Membuat fungsi dengan *args
def rekap_nilai(*args):
    rata_rata = sum(args) / len(args)
    tertinggi = max(args)
    terendah = min(args)
    return rata_rata, tertinggi, terendah

daftar_nilai = []

while True:
    input_nilai = input("Masukkan nilai ujian siswa (kosongkan untuk selesai): ")
    if input_nilai == "":
        break
    daftar_nilai.append(float(input_nilai))

if len(daftar_nilai) == 0:
    print("Data nilai tidak tersedia.")
else:
    # Membongkar list daftar_nilai ke dalam *args menggunakan tanda bintang
    rata, tertinggi, terendah = rekap_nilai(*daftar_nilai)
    
    print(f"Rata-rata kelas: {rata}")
    print(f"Nilai tertinggi: {int(tertinggi)} ")
    print(f"Nilai terendah: {int(terendah)} ")
    