@echo off
color c
title CALCULATOR BY Numenide
    ECHO APA YANG MAU KAU LAKUKAN?
    SET /P MAU="MAU APA?: "
    ECHO OALAH KAMU MAU %MAU%
    PAUSE/nul
    ECHO NAMUN KAMI HANYA BISA MEMBANTU MU UNTUK MENGHTIUNG!
    pause/nul
:menu
    set /p a1="Angka Pertama!:"
    set /p a2="Pilih Operator (*, /, -, +,) :"
    set /p a3="Angka Kedua :"
    set /a hasil= %a1% %a2% %a3%
    echo Hasil dari %a1% %a2% %a3% = %hasil%
    pause>nul
 goto :menu 