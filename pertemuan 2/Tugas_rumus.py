import math

print("=== PROGRAM RUMUS BANGUN DATAR ===")
print("1. Persegi")
print("2. Pythagoras")
print("3. Lingkaran")
print("4. Segitiga")
print("5. Persegi Panjang")

pilihan = int(input("Pilih rumus (1-5): "))

if pilihan == 1:
    sisi = float(input("Masukkan sisi persegi: "))

    luas = sisi * sisi
    keliling = 4 * sisi

    print("Luas persegi =", luas)
    print("Keliling persegi =", keliling)

elif pilihan == 2:
    print("=== Pythagoras ===")
    print("1. Mencari sisi miring")
    print("2. Mencari sisi tegak")
    print("3. Mencari sisi alas")

    pilih = int(input("Pilih (1-3): "))

    if pilih == 1:
        a = float(input("Masukkan sisi a: "))
        b = float(input("Masukkan sisi b: "))

        c = math.sqrt(a * a + b * b)
        print("Sisi miring =", c)

    elif pilih == 2:
        c = float(input("Masukkan sisi miring: "))
        a = float(input("Masukkan sisi alas: "))

        b = math.sqrt(c * c - a * a)
        print("Sisi tegak =", b)

    elif pilih == 3:
        c = float(input("Masukkan sisi miring: "))
        b = float(input("Masukkan sisi tegak: "))

        a = math.sqrt(c * c - b * b)
        print("Sisi alas =", a)

    else:
        print("Pilihan tidak tersedia.")

elif pilihan == 3:
    jari_jari = float(input("Masukkan jari-jari lingkaran: "))

    luas = math.pi * jari_jari * jari_jari
    keliling = 2 * math.pi * jari_jari

    print("Luas lingkaran =", luas)
    print("Keliling lingkaran =", keliling)

elif pilihan == 4:
    alas = float(input("Masukkan alas segitiga: "))
    tinggi = float(input("Masukkan tinggi segitiga: "))

    luas = 0.5 * alas * tinggi

    print("Luas segitiga =", luas)

elif pilihan == 5:
    panjang = float(input("Masukkan panjang: "))
    lebar = float(input("Masukkan lebar: "))

    luas = panjang * lebar
    keliling = 2 * (panjang + lebar)

    print("Luas persegi panjang =", luas)
    print("Keliling persegi panjang =", keliling)

else:
    print("Pilihan tidak tersedia.")