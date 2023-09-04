import pandas as pd

# Meminta input data dari user
name = input("Ngana pe nama panggil cth.(Fulan): ")
tgl = input("Masukkan tanggal setor cth.(01/01/2021): ")
ziyadah = input("Ziyadah Surat Apa cth.(Al-Fatihah: 1-7): ")
muro = input("Murojaah Surat Apa cth.(Al-Fatihah: 1-7): ")
hlmn = input("Barapa Halaman cth.(2 Halaman): ")
# Menentukan data yang akan disimpan dalam bentuk tabel
data = {
    'Tanggal Setoran': [tgl],
    'Ziyadah': [ziyadah],
    'Murojaah': [muro],
    'Halaman' : [hlmn],
}

# Membuat dataframe dari data
df = pd.DataFrame(data)

# Mengubah kolom tanggal menjadi objek tanggal
df['Tanggal Setoran'] = pd.to_datetime(df['Tanggal Setoran'], format='%d/%m/%Y')

# Mengakses informasi tanggal dan memformat menjadi bahasa Indonesia
df['Tanggal Setoran'] = df['Tanggal Setoran'].dt.strftime("%A, %d %B %Y")

# Menyimpan dataframe ke dalam file Excel
name = name + '.xlsx'
df.to_excel(name, index=False)
name = name
print('Hei', name, 'Data anda berhasil disimpan!')
