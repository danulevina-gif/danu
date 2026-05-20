# ============================================================
# PEMBAGIAN FUNGSI
# Anggota 1 - Muhammad Toro Haikal (2530801086) : tambah_buku(), tampilkan_buku(), cari_buku_rekursif(), jumlah_buku()
# Anggota 2 - MUhammad Adhitya RAmadan (2530108099) : pinjam_buku(), kembalikan_buku(), validasi_input(), menu_utama()
# ============================================================

buku = {}
riwayat = []

# =========================
# ANGGOTA 1
# =========================

def tambah_buku():
    kode = input("Kode Buku: ")
    judul = input("Judul Buku: ")

    try:
        stok = int(input("Stok: "))
    except ValueError:
        print("Stok harus angka!")
        return

    identitas = (kode, judul)

    buku[kode] = {
        "judul": judul,
        "stok": stok,
        "identitas": identitas
    }

    print("Buku berhasil ditambahkan!")


def tampilkan_buku():
    if not buku:
        print("Belum ada buku.")
        return

    for kode, data in buku.items():
        print(f"{kode} | {data['judul']} | Stok: {data['stok']}")


def cari_buku_rekursif(data_list, target, index=0):
    if index >= len(data_list):
        return None

    item = data_list[index]

    if item["judul"].lower() == target.lower():
        return item

    return cari_buku_rekursif(data_list, target, index + 1)


def jumlah_buku():
    total = len(buku)
    print(f"Total buku: {total}")

# =========================
# ANGGOTA 2
# =========================

def pinjam_buku():
    kode = input("Masukkan kode buku: ")

    if kode not in buku:
        print("Buku tidak ditemukan!")
        return

    if buku[kode]["stok"] <= 0:
        print("Stok habis!")
        return

    nama = input("Nama peminjam: ")

    buku[kode]["stok"] -= 1

    riwayat.append([kode, nama, "Dipinjam"])

    print("Buku berhasil dipinjam.")


def kembalikan_buku():
    kode = input("Kode buku: ")

    if kode not in buku:
        print("Buku tidak ditemukan!")
        return

    buku[kode]["stok"] += 1

    riwayat.append([kode, "-", "Dikembalikan"])

    print("Buku berhasil dikembalikan.")


def validasi_input():
    try:
        return int(input("Pilih menu: "))
    except ValueError:
        print("Input harus angka!")
        return -1


def menu_utama():
    while True:
        print("\n=== SISTEM PERPUSTAKAAN ===")
        print("1. Tambah Buku")
        print("2. Tampilkan Buku")
        print("3. Cari Buku")
        print("4. Pinjam Buku")
        print("5. Kembalikan Buku")
        print("6. jumlah buku")
        print("7. Keluar")

        pilihan = validasi_input()

        if pilihan == 1:
            tambah_buku()

        elif pilihan == 2:
            tampilkan_buku()

        elif pilihan == 3:
            target = input("Judul buku: ")

            data_list = list(buku.values())

            hasil = cari_buku_rekursif(data_list, target)

            if hasil:
                print("Buku ditemukan:", hasil)
            else:
                print("Buku tidak ditemukan.")

        elif pilihan == 4:
            pinjam_buku()

        elif pilihan == 5:
            kembalikan_buku()

        elif pilihan == 6:
            jumlah_buku()

        elif pilihan == 7:
            print("Program selesai.")
            break

        else:
            print("Menu tidak valid!")

menu_utama()