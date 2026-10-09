def cek_kata(teks, kata):
    indeks_list = []
    start = 0
    while True:
        pos = teks.lower().find(kata.lower(), start)
        if pos == -1:
            break
        indeks_list.append(pos)
        start = pos + 1
    return indeks_list

def cek_batas_kata(teks, i, panjang):
    alfabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    batas_kiri_aman = True
    batas_kanan_aman = True
    
    if i > 0:
        if teks[i - 1] in alfabet:
            batas_kiri_aman = False
            
    if i + panjang < len(teks):
        if teks[i + panjang] in alfabet:
            batas_kanan_aman = False
            
    return batas_kiri_aman and batas_kanan_aman

def sensor_kata(teks, kata, simbol):
    indeks_kotor = cek_kata(teks, kata)
    list_indeks_awal = []
    
    for i in indeks_kotor:
        if cek_batas_kata(teks, i, len(kata)):
            list_indeks_awal.append(i)
            
    teks_tersensor = ""
    last_idx = 0
    for i in list_indeks_awal:
        teks_tersensor += teks[last_idx:i] + (simbol * len(kata))
        last_idx = i + len(kata)
        
    teks_tersensor += teks[last_idx:]
    return teks_tersensor, len(list_indeks_awal), list_indeks_awal

print("--- Program Sensor ---")
teks = input("Masukkan Teks: ")
kata = input("Masukkan kata target: ")
simbol = input("Masukkan simbol: ")

hasil_teks, jumlah, indeks = sensor_kata(teks, kata, simbol)
print(f"Hasil Teks: {hasil_teks}")
print(f"Jumlah: {jumlah}  Indeks: {indeks}")

