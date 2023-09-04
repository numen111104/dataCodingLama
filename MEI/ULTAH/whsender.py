# Import library dan module yang dibutuhkan
import datetime
from whatsapp_api import Client

# Ambil waktu saat ini
now = datetime.datetime.now()

# Buat pesan dan kirim file .html sesuai dengan tanggal dan waktu yang diinputkan oleh pengguna
pesan = "Halo, ini adalah file html yang dikirimkan secara otomatis pada {} pada jam {}.".format(now.strftime("%d/%m/%Y"), now.strftime("%H:%M"))
client = Client()
path_file = "C:\\Users\\numan\\OneDrive\\Dokumen\\Belajar Coding\\ULTAH\\test.html"
client.sendfile("<+6285716895658>", path_file, pesan)
