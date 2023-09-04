#Penghitung Nilai PAS 
itqon = int (input("Nilai Itqon: "))
tajwid = int (input("Nilai Tajwid: " ))
adab = int (input("Nilai Adab: "))
#Hasil
AVERAGE = int (itqon + tajwid + adab) / 3
ROUND = round (AVERAGE,0)
#Output
print("Rata-Rata Nilai: ",ROUND)
