import requests
import os

def download_quranic_audio(no):
    # Format URL dengan input yang diberikan
    audio_url = f"https://download.quranicaudio.com/quran/bandar_baleela/complete/{no}.mp3"

    # Menentukan nama file audio berdasarkan nomor input pengguna
    file_name = f"{no}.mp3"

    # Menentukan path penyimpanan file audio
    save_directory = r"C:\Users\numan\OneDrive\Dokumen\DATA MUROTTAL\Sa'ad Al-Ghamidi"
    save_path = os.path.join(save_directory, file_name)

    # Membuat direktori penyimpanan jika belum ada
    os.makedirs(save_directory, exist_ok=True)

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

start_no = int(input("Masukkan NO awal: "))

for no in range(start_no, 115):
    download_quranic_audio(no)
