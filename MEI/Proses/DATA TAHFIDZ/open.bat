@echo off
color 0a
Echo SIMDAT v.0.1 by: Nu'man Nasyar MZ
Title SIMDAT v.0.1
echo.
echo.
:base
echo SIMPAN DATA TAHFIDZ v.0.1
echo ::::::::::::::::::::::::::MENU::::::::::::::::::::::::::
echo Menu:
echo 1. Daftar Data Baru
echo 2. Tambah Setoran Hafalan
set /p input=Masukkan pilihan dengan mengetik angka 1/2: 
if %input%==1 (
  data_baru.py
  goto :base
) else if %input%==2 (
  nambah.py
  echo.
  echo ========================END==========================
  echo.
  echo.
  type nide.txt
  goto :base
) else (
  echo.
  Echo Maaf, Anda memasukkan input yang tidak tertera.
  echo ========================END==========================
  echo.
  echo.
  type nide.txt
  goto :base
)

