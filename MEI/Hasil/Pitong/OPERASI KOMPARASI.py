# OPERASI KOMPARASI

puki = 5
nide = 4

# LEBIH BESAR DARI >
print('====== lebih besar dari (>)')
hasil = nide > 3
print(nide,'>', 3, "=", hasil)
hasil = puki > 5
print(puki, '>', 5, '=', hasil)
hasil = nide > 8 
print(puki, '>', 8, '=', hasil)
# LEBIH KECIL DARI <
print('====== lebih kecil dari (<)')
hasil = nide < 3
print(nide,'<', 3, "=", hasil)
hasil = puki < 5
print(puki, '<', 5, '=', hasil)
hasil = nide < 8 
print(puki, '<', 8, '=', hasil)
# LEBIH BESAR SAMA DENGAN DARI >=
print('====== lebih besar sama dengan dari (>=)')
hasil = nide >= 3
print(nide,'>=', 3, "=", hasil)
hasil = puki >= 5
print(puki, '>=', 5, '=', hasil)
hasil = nide >= 8 
print(puki, '>=', 8, '=', hasil)
# LEBIH KECIL SAMA DENGAN DARI <=
print('====== lebih kecil sama dengan dari (<=)')
hasil = nide <= 3
print(nide,'<=', 3, "=", hasil)
hasil = puki <= 5
print(puki, '<=', 5, '=', hasil)
hasil = nide <= 8 
print(puki, '<=', 8, '=', hasil)
# SAMA DENGAN ==
print('====== sama dengan dari (==)')
hasil = nide == 3
print(nide,'==', 3, "=", hasil)
hasil = puki == 5
print(puki, '==', 5, '=', hasil)
hasil = nide == 8 
print(puki, '==', 8, '=', hasil)
# TIDAK SAMA DENGAN !=
print('====== tidak sama dengan dari (!=)')
hasil = nide != 3
print(nide,'!=', 3, "=", hasil)
hasil = puki != 5
print(puki, '!=', 5, '=', hasil)
hasil = nide != 8 
print(puki, '!=', 8, '=', hasil)

# X=9 (X ADALAH OBJECT YANG MEMAKAN MEMORI)
# X+9 (9 ADALAH ANGKA LITERALLY)

# 'is' SEBAGAI KOMPARASI OBJECT IDENTITY
print('====== object sama dengan is')
N = 7 # INI ADALAH ASSINGMENT PEMBUATAN OBJECT
U = 7
print('Nilai N =',N,',','id= ',hex(id(N)))
print('Nilai U =',U,',','id= ',hex(id(U)))
hasil= N is U
print('N is U =',hasil)
# 'is not' SEBAGAI KOMPARASI OBJECT IDENTITY
print('====== object tidak sama dengan is not')
N = 7 # INI ADALAH ASSINGMENT PEMBUATAN OBJECT
U = 8
print('Nilai N =',N,'id= ',hex(id(N)))
print('Nilai U =',U,'id= ',hex(id(U)))
hasil= N is not U
print('N is U =',hasil)