# Anggap saja packages sebagai direktori Python scripts.
# Setiap script dapat dinamakan module
# Setiap module berisi fungsi, metode, dan tipe data tertentu
# Ribuan packages tersedia di Python seperti NumPy, Matplotlib, scikit-learn

# Instal packages menggunakan pip 
# pip adalah sebuah package installer untuk Python

# Untuk mendownload pip, bisa mengikuti petunjuk di https://pip.pypa.io/en/stable/installation/ 
# Kemudian download file get-pip.py
# Setelah itu, jalankan perintah berikut di terminal untuk menginstal pip:
# python get-pip.py

# Contoh penggunaan pip untuk menginstal package NumPy:
# pip install numpy

# Import packages
# Setelah menginstal package, kita dapat mengimpornya ke dalam script Python kita menggunakan perintah import.
# Contoh: import numpy

# Contoh Penggunaan package NumPy untuk membuat array:
import numpy
numpy.array([1, 2, 3, 4, 5])  # Output: array([1, 2, 3, 4, 5])

# Untuk memudahkan penggunaan package, kita bisa menggunakan alias dengan perintah as.
import numpy as np
np.array([1, 2, 3, 4, 5])  # Output: array([1, 2, 3, 4, 5])

# Jika hanya ingin menggunakan fungsi tertentu dari package, kita bisa mengimpor fungsi tersebut secara spesifik.
from numpy import array
array([1, 2, 3, 4, 5])  # Output: array([1, 2, 3, 4, 5])
# Notes: Kekurangannya adalah kita tidak bisa menggunakan fungsi lain dari package tersebut tanpa mengimpor ulang.