# NumPy singkatan dari Numeric Python
# Alternatif dari Python list: NumPy array
# Dapat melakukan kalkulasi semua array sekaligus yang merupakan keterbatasan dari Python list
# Lebih cepat daripada list

import numpy as np

np_height = np.array([1.73, 1.68, 1.71, 1.89, 1.79])
print(np_height)  # Output: [1.73 1.68 1.71 1.89 1.79]

np_weight = np.array([65.4, 59.2, 63.6, 88.4, 68.7])
print(np_weight)  # Output: [65.4 59.2 63.6 88.4 68.7]

bmi = np_weight / np_height ** 2
print(bmi)  # Output: [21.85171573 20.97505669 21.75028214 24.7473475  21.44127836]

# NumPy Remarks

remarks = np.array([1.0, "is", True])
print(remarks)  # Output: ['1.0' 'is' 'True']
# Notes: NumPy arrays hanya dapat menyimpan satu tipe data. Jika kita mencoba menyimpan tipe data yang berbeda, NumPy akan mengkonversi semuanya menjadi tipe data yang sama, biasanya string.

python_list = [1, 2, 3]
numpy_array = np.array([1, 2, 3])

python_list = python_list + python_list
print(python_list)  # Output: [1, 2, 3, 1, 2, 3]

numpy_array = numpy_array + numpy_array
print(numpy_array)  # Output: [2 4 6]
# Notes: Ketika kita menambahkan dua list, Python menggabungkan mereka. Namun, ketika kita menambahkan dua NumPy array, NumPy melakukan operasi penjumlahan elemen-wise, yaitu menjumlahkan elemen yang bersesuaian dari kedua array.

# NumPy Subsetting

print(bmi)
print(bmi[1])  # Output: 20.97505668934241

# Contoh lain penggunaan NumPy subsetting dengan menggunakan Boolean indexing
print(bmi > 23)  # Output: [False False False True False]
print(bmi[bmi > 23])  # Output: [24.7473475]

# Notes: Boolean indexing memungkinkan kita untuk memilih elemen-elemen dari array berdasarkan kondisi tertentu. Dalam contoh ini, kita memilih elemen-elemen dari array bmi yang lebih besar dari 23.