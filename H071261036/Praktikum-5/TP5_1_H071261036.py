def bersihkan_teks(teks):
    alfabet = "abcdefghijklmnopqrstuvwxyz"
    teks_bersih = ""
    for char in teks.lower():
        if char in alfabet:
            teks_bersih += char
    return teks_bersih

def cek_palinrome(teks):
    teks_terbalik = "".join(reversed(teks))
    if teks == teks_terbalik:
        return True, -1
    else:
        for i in range(len(teks)):
            if teks[i] != teks_terbalik[i]:
                return False, i
        return False, -1

def inti_palinrome(teks):
    teks_bersih = bersihkan_teks(teks)
    terpanjang = ""
    panjang_max = 0
    indeks_awal = 0
    
    for i in range(len(teks_bersih)):
        for j in range(i + 1, len(teks_bersih) + 1):
            substring = teks_bersih[i:j]
            if len(substring) > panjang_max:
                is_palin, _ = cek_palinrome(substring)
                if is_palin:
                    panjang_max = len(substring)
                    terpanjang = substring
                    indeks_awal = i
                    
    return {"teks": terpanjang, "panjang": panjang_max, "indeks_awal": indeks_awal}

print("--- Program Pencari Palindrom ---")
teks_input = input("Masukkan teks prasasti: ")
bersih = bersihkan_teks(teks_input)
print(f"Teks Bersih: {bersih}")
hasil = inti_palinrome(teks_input)
print(f"Output Terharap: {hasil}")
