#INTEGRAL# Adalah angka biasa tanpa koma
print("#####INTEGRAL KE YANG LAEN#####")
integral = 1 
print( integral ,"Adalah",type(integral))
# Dari Integral Ubah ke Float
integral_ke_float = float(integral)
print( integral_ke_float, "Adalah", type(integral_ke_float))
# Dari Integral Ubah ke String (Teks/Kararakter)
integral_ke_string = str(integral)
print(integral_ke_string, "Adalah", type(integral_ke_string))
# Dari Integral ubah ke Boolean (True/False)
internal_ke_boolean = bool(integral) # Hasil False hanya dari castingan angka nol
print(internal_ke_boolean, "Adalah", type(internal_ke_boolean)) 

#STRING# Adalah Chararacter/Teks
print("######STRING KE YANG LAIN#####")
string = "0"
print(string, "Adalah", type(string))
# Dari String ubah ke Integral
string_ke_integral = int(string) # Hanya bisa dicasting kalau string nya berupa angka
print(string_ke_integral, "Adalah", type(string_ke_integral)) 
# Dari String ubah ke Float
string_ke_float = float(string) # Hanya bisa dicasting kalau string nya berupa angka
print(string_ke_float, "Adalah", type(string_ke_float))
# Dari String ubah ke Boolean 
string_ke_boolean = bool(string) # Hasil False hanya didapatkan ketika string nya kosong ""
print(string_ke_boolean, "Adalah", type(string_ke_boolean))

#FLOAT# Adalah angka yang memiliki koma exm = 0.0
print("#####FLOAT KE YANG LAEN#####")
Float = 1.9
print(Float, "Adalah", type(Float))
# Dari Float ubah ke Integral
float_ke_integral = int(Float) # Akan dibulatkan kebawah
print(float_ke_integral, "Adalah", type(float_ke_integral))
# Dari Float ubah ke String
float_ke_string = str(Float)
print(float_ke_string, "Adalah", type(float_ke_string))
# Dari Float ubah ke Boolean
float_ke_boolean = bool(Float) # Hasil False hanya ketika floatnya 0
print(float_ke_boolean, "Adalah", type(float_ke_boolean))

#BOOLEAN# Adalah True/False. False hanya berlaku ketika data integral = 0, float = 0 / 0.0, string = kosong, boolean
print("######BOOLEAN KE YANG LAEN######")
boolean = False
print(boolean, "Adalah", type(boolean))
# Dari Boolean ubah ke Integral
boolean_ke_integral = int(boolean)
print(boolean_ke_integral, "Adalah", type(boolean_ke_integral))
# Dari Boolean ubah ke Float
boolean_ke_float = float(boolean)
print(boolean_ke_float, "Adalah", type(boolean_ke_float))
# Dari Boolean ubah ke String
boolean_ke_string = str(boolean)
print(boolean_ke_string, "Adalah", type(boolean_ke_string))
