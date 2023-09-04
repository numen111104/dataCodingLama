# menambahkan input baru ke file
file = open("namafile.txt", "w")  # buka file dengan mode "w" (write)
file.write("input baru")  # menambahkan input baru ke file
file.close()  # tutup file

# mengedit input yang sudah ada di file
file = open("namafile.txt", "r+")  # buka file dengan mode "r+" (read dan write)
isi_file = file.read()  # baca isi file
isi_file = isi_file.replace("input lama", "input baru")  # edit input yang sudah ada
file.seek(0)  # kembali ke awal file
file.write(isi_file)  # tulis isi file yang sudah diedit
file.close()  # tutup file

#WITH
nama = input("Siapa Namamu: ")
with open('nama_pengguna.txt', 'w') as file:
    file.write(nama)