
import json
import os
from datetime import datetime

FILE_DATA = "profil_data.json"          # File penyimpanan eksternal
LEBAR = 50                              # Lebar kartu profil di terminal
KATEGORI = ["Mahasiswa", "Pelajar", "Karyawan", "Wirausaha", "Lainnya"]


# ======================================================================
# BAGIAN 1: PENYIMPANAN DATA (JSON)
# ======================================================================
def muat_data():
    """Membaca data dari file JSON. Mengembalikan list kosong jika
    file belum ada atau rusak."""
    if not os.path.exists(FILE_DATA):
        return []
    try:
        with open(FILE_DATA, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        print("[!] File data tidak terbaca, memulai dengan data kosong.")
        return []


def simpan_data(data):
    """Menulis seluruh list profil ke file JSON."""
    with open(FILE_DATA, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def buat_id(data):
    """Membuat ID unik berurutan (U001, U002, ...) berdasarkan ID terbesar."""
    angka = [int(p["id"][1:]) for p in data if p["id"][1:].isdigit()]
    return f"U{(max(angka) + 1 if angka else 1):03d}"


# ======================================================================
# BAGIAN 2: VALIDASI INPUT
# ======================================================================
def valid_email(teks):
    """Email valid: tanpa spasi, mengandung '@' dan '.' setelah '@'."""
    if " " in teks or teks.count("@") != 1:
        return False
    lokal, domain = teks.split("@")
    return bool(lokal) and "." in domain and not domain.startswith(".") \
        and not domain.endswith(".")


def valid_telepon(teks):
    """Nomor telepon: hanya angka, panjang 8-15 digit."""
    return teks.isdigit() and 8 <= len(teks) <= 15


def valid_tanggal(teks):
    """Tanggal lahir format DD-MM-YYYY, tidak boleh di masa depan."""
    try:
        tgl = datetime.strptime(teks, "%d-%m-%Y")
        return tgl <= datetime.now()
    except ValueError:
        return False


def valid_gender(teks):
    """Jenis kelamin: L atau P."""
    return teks.upper() in ("L", "P")


def minta_input(label, validator=None, pesan_error="Input tidak valid.",
                wajib=True, ubah=lambda x: x):
    """Meminta input berulang sampai valid.
    - wajib=True  : tidak boleh kosong
    - validator   : fungsi pengecek format (opsional)
    - ubah        : fungsi transformasi hasil (mis. huruf besar)"""
    while True:
        nilai = input(f"{label}: ").strip()
        if not nilai:
            if wajib:
                print("  [!] Input tidak boleh kosong.")
                continue
            return "-"
        if validator and not validator(nilai):
            print(f"  [!] {pesan_error}")
            continue
        return ubah(nilai)


def pilih_kategori():
    """Menampilkan pilihan kategori dan mengembalikan pilihan yang valid."""
    print("Status/Kategori:")
    for i, k in enumerate(KATEGORI, 1):
        print(f"  {i}. {k}")
    pilihan = minta_input(
        "Pilih nomor", lambda x: x.isdigit() and 1 <= int(x) <= len(KATEGORI),
        f"Pilih angka 1-{len(KATEGORI)}.")
    return KATEGORI[int(pilihan) - 1]


# ======================================================================
# BAGIAN 3: TAMPILAN
# ======================================================================
def tampilkan_kartu(p):
    """Mencetak satu profil dalam bentuk kartu terminal."""
    gender = "Laki-laki" if p["jenis_kelamin"] == "L" else "Perempuan"
    baris = [
        ("ID", p["id"]), ("Nama", p["nama"]), ("Email", p["email"]),
        ("Telepon", p["telepon"]), ("Tgl Lahir", p["tanggal_lahir"]),
        ("Gender", gender), ("Alamat", p["alamat"]),
        ("Status", p["status"]), ("Hobi", p["hobi"]),
        ("Ket.", p["keterangan"]),
    ]
    print("+" + "=" * (LEBAR - 2) + "+")
    print("|" + "KARTU PROFIL".center(LEBAR - 2) + "|")
    print("+" + "=" * (LEBAR - 2) + "+")
    for label, isi in baris:
        teks = f" {label:<10}: {isi}"
        print("|" + teks[:LEBAR - 3].ljust(LEBAR - 2) + "|")
    print("+" + "=" * (LEBAR - 2) + "+")


def garis(judul):
    """Mencetak judul bagian."""
    print("\n" + "-" * LEBAR)
    print(judul.center(LEBAR))
    print("-" * LEBAR)


# ======================================================================
# BAGIAN 4: FITUR UTAMA
# ======================================================================
def registrasi(data):
    """Form registrasi: meminta semua field, memvalidasi, lalu menyimpan."""
    garis("REGISTRASI DATA BARU")
    nama = minta_input("Nama Lengkap", ubah=str.title)
    email = minta_input("Email", valid_email,
                        "Email harus mengandung '@' dan '.' (contoh: a@b.com).",
                        ubah=str.lower)
    # Cegah email ganda
    if any(p["email"] == email for p in data):
        print("[!] Email sudah terdaftar. Registrasi dibatalkan.")
        return
    telepon = minta_input("Nomor Telepon (angka saja)", valid_telepon,
                          "Nomor harus angka, 8-15 digit.")
    tgl = minta_input("Tanggal Lahir (DD-MM-YYYY)", valid_tanggal,
                      "Format harus DD-MM-YYYY dan bukan tanggal masa depan.")
    gender = minta_input("Jenis Kelamin (L/P)", valid_gender,
                         "Ketik L atau P.", ubah=str.upper)
    alamat = minta_input("Alamat")
    status = pilih_kategori()
    hobi = minta_input("Hobi (pisahkan dengan koma)")
    ket = minta_input("Keterangan profil (opsional, Enter untuk lewati)",
                      wajib=False)

    profil = {
        "id": buat_id(data), "nama": nama, "email": email,
        "telepon": telepon, "tanggal_lahir": tgl, "jenis_kelamin": gender,
        "alamat": alamat, "status": status, "hobi": hobi, "keterangan": ket,
    }
    data.append(profil)
    simpan_data(data)
    print(f"\n[✓] Registrasi berhasil! ID Anda: {profil['id']}")
    tampilkan_kartu(profil)


def lihat_cari(data):
    """Submenu: tampilkan semua profil atau cari berdasarkan ID/Nama."""
    garis("LIHAT / CARI PROFIL")
    if not data:
        print("Belum ada data terdaftar.")
        return
    print("1. Lihat semua profil\n2. Cari berdasarkan ID/Nama")
    pilihan = minta_input("Pilih", lambda x: x in ("1", "2"), "Pilih 1 atau 2.")
    if pilihan == "1":
        hasil = data
    else:
        kata = minta_input("Masukkan ID atau Nama").lower()
        hasil = [p for p in data
                 if kata == p["id"].lower() or kata in p["nama"].lower()]
    if not hasil:
        print("[!] Data tidak ditemukan.")
        return
    print(f"\nDitemukan {len(hasil)} profil:\n")
    for p in hasil:
        tampilkan_kartu(p)
        print()


def hapus(data):
    """Menghapus profil berdasarkan ID, dengan konfirmasi."""
    garis("HAPUS DATA")
    if not data:
        print("Belum ada data terdaftar.")
        return
    id_cari = minta_input("Masukkan ID yang akan dihapus").upper()
    target = next((p for p in data if p["id"] == id_cari), None)
    if not target:
        print("[!] ID tidak ditemukan.")
        return
    tampilkan_kartu(target)
    yakin = minta_input("Yakin hapus data ini? (y/n)",
                        lambda x: x.lower() in ("y", "n"), "Ketik y atau n.")
    if yakin.lower() == "y":
        data.remove(target)
        simpan_data(data)
        print("[✓] Data berhasil dihapus.")
    else:
        print("Penghapusan dibatalkan.")


# ======================================================================
# BAGIAN 5: MENU UTAMA
# ======================================================================
def menu_utama():
    """Perulangan menu utama sampai pengguna memilih keluar."""
    data = muat_data()
    while True:
        garis("SISTEM PROFIL PENGGUNA")
        print("1. Registrasi Data Baru")
        print("2. Lihat Semua Profil / Cari Profil")
        print("3. Hapus Data")
        print("4. Keluar Program")
        pilihan = input("\nPilih menu (1-4): ").strip()

        if pilihan == "1":
            registrasi(data)
        elif pilihan == "2":
            lihat_cari(data)
        elif pilihan == "3":
            hapus(data)
        elif pilihan == "4":
            print("Terima kasih! Data tersimpan di", FILE_DATA)
            break
        else:
            print("[!] Pilihan tidak valid, masukkan angka 1-4.")


if __name__ == "__main__":
    try:
        menu_utama()
    except (KeyboardInterrupt, EOFError):
        print("\nProgram dihentikan.")