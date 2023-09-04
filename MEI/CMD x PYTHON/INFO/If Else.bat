@echo off
::IF ELSE
Title "IF ELSE"
    echo Easier Trial
    echo.
:menu
    set n2=Makan
    set n1=Makan
    set n=Nilai Variabel Tidak Sama
    set b=Nilai Variabel Sama
  IF %n1%==%n2% (
      echo Hasil %n2%:%n1% == %b%
  ) else (
      echo Hasil %n2%:%n1% == %n%
  )
  pause>nul
  goto:menu