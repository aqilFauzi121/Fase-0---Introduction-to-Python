# functions adalah fungsi bawaan Python yang digunakan untuk melakukan operasi tertentu pada data atau objek.
# contoh: max(), round()
# cara mempelajari penggunaan functions adalah menggunakan perintah help(), contoh: help(max)
# bisa juga mencari dokumentasi resmi di https://docs.python.org/3/library/functions.html

# Max function
# Menggunakan max() untuk mendapatkan nilai maksimum dari sebuah list
angka = [10, 5, 8, 20, 15]
nilai_maksimum = max(angka)
print("Nilai maksimum dari list angka adalah:", nilai_maksimum)  # Output: 20

# Round function
# Menggunakan round() untuk membulatkan angka desimal
nilai_desimal = 7.65
nilai_bulat = round(nilai_desimal)
print("Nilai bulat dari", nilai_desimal, "adalah:", nilai_bulat)  # Output: 8

nilai_desimal_2 = 4.32
nilai_bulat_2 = round(nilai_desimal_2, 1)  # Membulatkan hingga 1 angka di belakang koma
print("Nilai bulat dari", nilai_desimal_2, "adalah:", nilai_bulat_2)  # Output: 4.3

nilai_desimal_3 = 9.8765
nilai_bulat_3 = round(nilai_desimal_3, 3)  # Membulatkan hingga 3 angka di belakang koma
print("Nilai bulat dari", nilai_desimal_3, "adalah:", nilai_bulat_3)  # Output: 9.877

# Notes: Fungsi max() mengembalikan nilai terbesar dari sebuah iterable seperti list atau tuple.
# Fungsi round() membulatkan angka desimal ke bilangan bulat terdekat.