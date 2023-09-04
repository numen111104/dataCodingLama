#SAVE USER INPUT#
#DATA ASK
nama = input("Apa Nama Panjang Anda: ")
ttl = input("Apa Tempat, Tanggal, Lahir Anda: ")
sekolah = input("Apa Nama Sekolah Anda: ")
emel_id = input("Apa ID Game MLBB Anda: ")
emel_server = input("Apa Server Game MLBB Anda: ")
print("Nama: ", nama,
      "Tempat, Tanggal Lahir: ", ttl,
      "Asal Sekolah: ", sekolah,
      "ID Game Mobile Legends: ", emel_id,
      "Server Game: ", emel_server)

#SIMPAN MEngunakan WRITE

with open('output.txt', 'w') as file:
    file.write(nama)
    file.writelines
    file.write(ttl)
    file.write(sekolah)
    file.write(emel_id)
    file.write(emel_server)

