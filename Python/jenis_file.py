import os

def ubah_nama_file(nama_file, nama_baru):
    direktori = r"C:\Users\numan\OneDrive\Dokumen\Belajar Coding\Python\IMAGES_DOWNLOAD"
    path_lama = os.path.join(direktori, nama_file)
    path_baru = os.path.join(direktori, nama_baru)

    try:
        os.rename(path_lama, path_baru)
        print("Nama file berhasil diubah.")
    except OSError:
        print("Terjadi kesalahan saat mengubah nama file.")

# Contoh penggunaan
nama_file = input("Masukkan nama file yang ingin diubah: ")
nama_baru = input("Masukkan nama baru untuk file: ")

ubah_nama_file(nama_file, nama_baru)
