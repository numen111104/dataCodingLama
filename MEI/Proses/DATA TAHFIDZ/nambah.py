from unicodedata import name
import pandas as pd

# Meminta input data dari user
name = input("Masukkan Nama sesuai Data: ")
name = name + '.xlsx'
tgl_baru = input("Masukkan tanggal setor baru cth.(01/01/2021): ")
ziyadah_baru = input("Ziyadah Surat Baru Apa cth.(Al-Fatihah: 1-7): ")
muro_baru = input("Murojaah Surat Baru Apa cth.(Al-Fatihah: 1-7): ")
hlmn_baru = input("Barapa Halaman Baru cth.(2 Halaman): ")

# Menentukan data baru yang akan ditambahkan
data_baru = {
    'Tanggal Setoran': [tgl_baru],
    'Ziyadah': [ziyadah_baru],
    'Murojaah': [muro_baru],
    'Halaman' : [hlmn_baru],
}

df = pd.read_excel(name)

# Membuat data frame baru dari data
df_baru = pd.DataFrame(data_baru)

# Mengubah kolom tanggal menjadi objek tanggal pada data frame baru
df_baru['Tanggal Setoran'] = pd.to_datetime(df_baru['Tanggal Setoran'], format='%d/%m/%Y')

# Mengakses informasi tanggal dan memformat menjadi bahasa Indonesia pada data frame baru
df_baru['Tanggal Setoran'] = df_baru['Tanggal Setoran'].dt.strftime("%d %B %Y")

# Menggabungkan data frame lama dan data frame baru
df = pd.concat([df, df_baru])

# Menyimpan data frame yang baru saja digabungkan ke dalam file Excel
df.to_excel(name, index=False)

print('Data berhasil ditambahkan dan disimpan dalam file Excel!')
