persentase = int(input("Masukkan persentase cabai: "))

if persentase < 0:
    print("Input tidak valid")
elif persentase <= 10:
    print("Level Aman")
elif persentase <= 70:
    print("Level Pedas")
elif persentase <= 40:
    print("Level Sedang")
else:
    print("Level Ekstrem")
    