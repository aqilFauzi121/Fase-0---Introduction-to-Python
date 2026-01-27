#LIST

anggota_tubuh = ["kepala", "mata", "telinga", "hidung", "mulut"]
print(anggota_tubuh)
print(type(anggota_tubuh))


warna = [["pulpen", "merah"], ["buku", "biru"], ["tas", "hitam"]]
print(warna)
print(type(warna))

tinggi_badan = [["budi", 175], ["ani", 160], ["citra", 168]] # dalam cm
print(tinggi_badan)
print(type(tinggi_badan), "\n")

#SUBSTETING LIST

#Index
print(anggota_tubuh[0])    # Output: kepala
print(warna[1][1])         # Output: biru
print(tinggi_badan[2][0], "\n")  # Output: citra

#Negative Index
print(anggota_tubuh[-5])   # Output: kepala
print(warna[-2][-1])        # Output: biru
print(tinggi_badan[-1][-2], "\n") # Output: citra

# Notes: Negative index menghitung dari belakang, dimulai dari -1 untuk elemen terakhir.

#Slicing
print(anggota_tubuh[1:4])  # Output: ['mata', 'telinga', 'hidung']
print(warna[0:2])          # Output: [['pulpen', 'merah'], ['buku', 'biru']]
print(tinggi_badan[0:2], "\n")   # Output: [['budi', 175], ['ani', 160]]

# Notes: Untuk slicing, indeks awal dimasukkan dan indeks akhir tidak dimasukkan; 
# Misal, anggota_tubuh[1:4] mengambil elemen dari indeks 1 sampai 3, indeks 4 tidak dimasukkan.