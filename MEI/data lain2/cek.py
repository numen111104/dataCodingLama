import sqlite3
import datetime

# set jumlah kesempatan maksimal
max_attempt = 3
# set nama dan password yang benar
username = 'NUMENIDE'
password = '191104'
# inisialisasi jumlah percobaan
attempt_count = 0

while attempt_count < max_attempt:
    # minta input nama dan password dari user
    user_input_name = input("Masukkan Nama: ")
    user_input_password = input("Masukkan Password: ")
    
    # cek apakah nama dan password sesuai
    if user_input_name == username and user_input_password == password:
        # membuat koneksi ke database
        conn = sqlite3.connect('nilaitajwid.db')

        # membuat cursor
        cur = conn.cursor()

        # mengambil semua data dari tabel nilaitajwid
        cur.execute("SELECT * FROM nilaitajwid")
        rows = cur.fetchall()

        # menampilkan data
        for row in rows:
            print(row)

        # menutup koneksi
        conn.close()
        
        # keluar dari loop while karena login berhasil
        break
    else:
        # menambah jumlah percobaan
        attempt_count += 1
        # jika sudah mencapai batas percobaan maksimal, buat file error.txt
        if attempt_count == max_attempt:
            print("\nMaaf anda bukan tuan Nu'man Nasyar MZ, Saya akan laporkan Anda!!\n")
            now = datetime.datetime.now()
            with open("C:\\Users\\numan\\OneDrive\\Dokumen\\Pengabdian\\Pelajaran Tajwid\\Nilai\\Log\\CEKERROR" + str(now.date()) + "-" + str(now.time()).split(".")[0].replace(":","-") + ".txt", "w") as file:
                file.write(f"Nama dan Password salah. Nama: {user_input_name}, Password: {user_input_password}, Waktu: {datetime.datetime.now()}")
        else:
            # jika masih ada kesempatan, tampilkan pesan kesalahan
            print("Nama atau Password salah. Silahkan coba lagi.")

