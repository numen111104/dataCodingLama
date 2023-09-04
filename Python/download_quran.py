import requests
import os

def download_quranic_audio(no, folder_name):
    # Format nomor surat dengan padding nol hingga 3 digit
    no_padded = str(no).zfill(3)

    # Format URL dengan input yang diberikan
    audio_url = f"https://download.quranicaudio.com/quran/bandar_baleela/complete/{no_padded}.mp3"

    # Menentukan nama file audio berdasarkan nomor input pengguna
    file_name = f"{no_padded}.mp3"

    # Menentukan path penyimpanan folder
    save_directory = fr"C:\Users\numan\OneDrive\Dokumen\DATA MUROTTAL\{folder_name}"
    os.makedirs(save_directory, exist_ok=True)

    # Menentukan path penyimpanan file audio
    save_path = os.path.join(save_directory, file_name)

    # Melakukan permintaan HTTP GET untuk mengunduh audio
    response = requests.get(audio_url)

    # Memeriksa apakah permintaan berhasil
    if response.status_code == 200:
        # Menyimpan file audio
        with open(save_path, "wb") as file:
            file.write(response.content)
        print(f"Audio {file_name} berhasil diunduh dan disimpan di {save_path}")
    else:
        print(f"Gagal mengunduh audio.")

# Input dari pengguna
folder_name = input("Masukkan nama folder: ")

# Memanggil fungsi download_quranic_audio untuk setiap nomor surat dari 1 hingga 114
for no in range(1, 115):
    download_quranic_audio(no, folder_name)
