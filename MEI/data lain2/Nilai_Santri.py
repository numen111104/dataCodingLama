from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import datetime
import getpass

Base = declarative_base()

class NilaiTajwid(Base):
    __tablename__ = 'nilaitajwid'
    id = Column(Integer, primary_key=True)
    nama_santri = Column(String)
    nilai = Column(String)
    tanggal = Column(DateTime)

engine = create_engine('sqlite:///nilaitajwid.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

print("\n"+"="*60)
print("SELAMAT DATANG DI SISTEM PENDATAAN NILAI TAJWID")
print("="*60+"\n")

# buat variabel untuk menyimpan jumlah percobaan input nama dan password
num_tries = 0

while num_tries < 3:
    nama = input("Masukkan Nama: ")
    password = getpass.getpass(prompt='Masukkan Password: ')

    if nama == "NUMENIDE" and password == "191104":
        print("\nAnda berhasil login!\n")
        nama_santri = input("Nama Santri: ")
        nilai = input("Nilai: ")

        data = input("Apakah ini data lama atau baru?: ")
        if data.lower() == "baru":
            tanggal = datetime.datetime.now()
        elif data.lower() == "lama":
            tanggal_input = input("Masukkan tanggal dengan format dd/mm/yyyy: ")
            tanggal = datetime.datetime.strptime(tanggal_input, "%d/%m/%Y")
        else:
            print("Masukkan data dengan benar!")
            tanggal = None

        if tanggal is not None:
            try:
                new_row = NilaiTajwid(nama_santri=nama_santri, nilai=nilai, tanggal=tanggal)
                session.add(new_row)
                session.commit()
                print("\nData baru berhasil disimpan.\n")
            except Exception as e:
                print("\nTerjadi kesalahan saat menyimpan data baru:", e, "\n")
                session.rollback()
        else:
            print("\nTidak ada data yang disimpan.\n")
        
        # keluar dari loop karena user telah berhasil login
        break

    else:
        num_tries += 1
        if num_tries < 3:
            print("\nNama atau password salah. Anda memiliki", 3 - num_tries, "percobaan lagi.\n")
        else:
            print("\nMaaf anda bukan tuan Nu'man Nasyar MZ, Saya akan laporkan Anda!!\n")
            now = datetime.datetime.now()
            with open("C:\\Users\\numan\\OneDrive\\Dokumen\\Pengabdian\\Pelajaran Tajwid\\Nilai\\Log\\ERRORLOGIN" + str(now.date()) + "-" + str(now.time()).split(".")[0].replace(":","-") + ".txt", "w") as file:
                file.write("Tanggal Error: " + str(now.date()) + "\n")
                file.write("Waktu Error: " + str(now.time()).split(".")[0] + "\n")
                file.write("Nama Setan = " + nama + "\n")
                file.write("Password Setan = " + password)
                file.write("Alasan: Data yang dimasukkan tidak benar, harap berhati-hati\n")
