@echo off
color 1e
echo ********** DATA INPUT LATIHAN *********
echo.
:menu
    set /p fln="Mau Nama Apa filenya?: "
    md %fln%
goto:menu
