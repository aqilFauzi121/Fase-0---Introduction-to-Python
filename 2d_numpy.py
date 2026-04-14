# NumPy 2D
import numpy as np

np_2d = np.array([[1.73, 1.68, 1.71, 1.89, 1.79], 
                  [65.4, 59.2, 63.6, 88.4, 68.7]])

print(np_2d) 
# Output:
# [[1.73 1.68 1.71 1.89 1.79]
#  [65.4 59.2 63.6 88.4 68.7]]

print(np_2d.shape)  # Output: 2 rows, 5 columns

np.array = np.array([[1.73, 1.68, 1.71, 1.89, 1.79], 
                  [65.4, 59.2, 63.6, 88.4, "68.7"]])

print(np_2d)
# Output:
# [['1.73' '1.68' '1.71' '1.89' '1.79']
#  ['65.4' '59.2' '63.6' '88.4' '68.7']]
# Notes: Ketika kita mencoba menyimpan tipe data yang berbeda dalam sebuah array, NumPy akan mengkonversi semuanya menjadi tipe data yang sama, dalam hal ini string.

# NumPy Subsetting

print(np_2d[0])  # Output: [1.73 1.68 1.71 1.89 1.79]
print(np_2d[0][2])  # Output: 1.71
print(np_2d[0, 2])  # Output: 1.71

print(np_2d[:, 1:3]) 
# Output:
# [[ 1.68  1.71]
#  [59.2  63.6 ]]

print(np_2d[1, :]) # Output: [65.4 59.2 63.6 88.4 68.7]