@echo off
color 4
title NUMENIDE.exe
echo NUMENIDE v.1
echo.
echo.
echo Selamat Datang di NUMENIDE, Apa yang bisa saya bantu;
:Menu
echo 1. Menghitung Nilai PAS "20%"
echo 2. Menghitung Nilai UTS "10%"
echo 3. Menghitung Nilai Harian "70%"
set /p input="Nomor berapa yang anda pilih:"
if %input%==1 (
goto :PAS
) else if %input%==2 ( 
goto :UTS
) else if %input%==3 (
goto :NH
) else (
goto :WRONG
)
goto :Menu

:PAS
start pas.bat
goto :Menu

:UTS
start uts.bat
goto :Menu

:NH
start nh.bat
goto :Menu
