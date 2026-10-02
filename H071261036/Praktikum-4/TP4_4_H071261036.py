def konversi_suhu(suhu, asal, tujuan):
    skala_valid = ['C', 'F', 'K']
    
    # Memicu error secara manual jika skala tidak ada di daftar
    if asal not in skala_valid or tujuan not in skala_valid:
        raise ValueError("Error: Fadel.")
    
    # Ubah suhu asal ke Celsius dulu agar rumusnya lebih mudah
    if asal == 'C':
        suhu_c = suhu
    elif asal == 'F':
        suhu_c = (suhu - 32) * 5/9
    elif asal == 'K':
        suhu_c = suhu - 273.15
        
    # Ubah dari Celsius ke skala tujuan
    if tujuan == 'C':
        hasil = suhu_c
    elif tujuan == 'F':
        hasil = (suhu_c * 9/5) + 32
    elif tujuan == 'K':
        hasil = suhu_c + 273.15
        
    return hasil

print("=== Konversi Suhu ===")
while True:
    input_suhu = input("Masukkan suhu (atau 'selesai' untuk keluar): ")
    if input_suhu.lower() == 'selesai':
        break
        
    suhu = float(input_suhu)
    asal = input("Skala asal (C/F/K): ").upper()
    tujuan = input("Skala tujuan (C/F/K): ").upper()
    
    try:
        hasil = konversi_suhu(suhu, asal, tujuan)
        print(f"Hasil: {suhu} {asal} = {hasil} {tujuan}")
    except ValueError:
        print("Error: Skala suhu tidak dikenali.")
         