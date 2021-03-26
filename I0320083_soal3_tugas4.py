# Program Pemeriksaan Berat Bagasi

# input data berat bagasi
X = berat_maksimum_lbs = 50
Y = berat_maksimum_kg = X*0.453592
A = berat_a = 110
B = berat_b = 49

# output seleksi berat a
seleksi_a = Y>=A
print(seleksi_a)

# output seleksi berat b
seleksi_b = Y>=B
print(seleksi_b)