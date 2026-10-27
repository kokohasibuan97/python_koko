
nama = input("Masukkan nama mahasiswa: ")
nilai = float(input("Masukkan nilai mahasiswa: "))

if nilai < 0 or nilai > 100:
    print("Nilai tidak valid")
elif nilai >= 85:
    print("Nama:", nama)
    print("Status: Lulus")
    print("Predikat: A")
elif nilai >= 75:
    print("Nama:", nama)
    print("Status: Lulus")
    print("Predikat: B")
elif nilai >= 60:
    print("Nama:", nama)
    print("Status: Lulus")
    print("Predikat: C")
else:
    print("Nama:", nama)
    print("Status: Tidak Lulus")
    print("Predikat: D")

