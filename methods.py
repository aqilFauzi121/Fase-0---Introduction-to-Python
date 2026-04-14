# Methods: Sebuah fungsi yang dimiliki oleh objek tertentu
# Everything = object
# Objects memiliki associated methods, tergantung tipe data nya

# example of methods in type str: capitalize(), replace()
# example of methods in type float: bit_length(), conjugate()
# example of methods in type list: index(), count()

# List Methods
fam = ['liz', 1.73, 'emma', 1.68, 'mom', 1.71, 'dad', 1.89]
print(fam.count(1.73))  # mengembalikan nilai 1, karena hanya liz yang tinggi nya 1.73m
print(fam.index('mom'))  # mengembalikan nilai 4, karena 'mom' berada di index 4

print(dir(list))  # Menampilkan semua metode yang tersedia untuk objek list.
print(help(list.count))  # menampilkan dokumentasi untuk metode count


# String Methods
sister = 'liz'
print(sister.capitalize())  # mengembalikan nilai 'Liz', mengkapitalisasi huruf pertama
print(sister.replace('z', 'sa'))  # mengembalikan nilai 'lisa', mengganti 'z' dengan 'sa'

print(dir(str))  # menampilkan semua metode yang tersedia untuk objek string
print(help(str.capitalize))  # menampilkan dokumentasi untuk metode capitalize