import requests
import os

def download_image(url, save_directory):
    response = requests.get(url)
    if response.status_code == 200:
        # Mengambil nama file dari URL
        filename = url.split("/")[-1]
        save_path = os.path.join(save_directory, filename)

        # Memeriksa apakah file dengan nama yang sama sudah ada di direktori tujuan
        if os.path.exists(save_path):
            ganti_nama = input("File dengan nama yang sama sudah ada. Apakah Anda ingin mengganti nama file? (ya/tidak): ")
            if ganti_nama.lower() == "ya":
                nama_baru = input("Masukkan nama baru: ")
                save_path = os.path.join(save_directory, nama_baru)
            else:
                print("Gambar tidak diunduh.")
                return

        with open(save_path, 'wb') as file:
            file.write(response.content)
        print("Gambar berhasil diunduh.")
    else:
        print("Terjadi kesalahan saat mengunduh gambar.")

# Input URL gambar
url = input("Masukkan URL gambar: ")

# Path penyimpanan
save_directory = r"C:\Users\numan\OneDrive\Dokumen\Belajar Coding\Python\IMAGES_DOWNLOAD"

# Memanggil fungsi download_image
download_image(url, save_directory)
