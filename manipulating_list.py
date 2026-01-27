# Change list elements
# Add list elements
# Remove list elements

# Changing one list elements
tinggi_badan = [["budi", 175], ["ani", 160], ["citra", 168]] # dalam cm
tinggi_badan[1][1] = 158
print(tinggi_badan, "\n")  # Output: [['budi', 175], ['ani', 158], ['citra', 168]]

# Changing beberapa list elements
anggota_tubuh = ["kepala", "mata", "telinga", "hidung", "mulut"]
anggota_tubuh[1:4] = ["leher", "bahu", "lengan"]
print(anggota_tubuh, "\n")  # Output: ['kepala', 'leher', 'bahu', 'lengan', 'mulut']

# Adding list elements
anggota_tubuh = anggota_tubuh + ["kaki"]
print(anggota_tubuh, "\n")  # Output: ['kepala', 'leher', 'bahu', 'lengan', 'mulut', 'kaki']

anggota_tubuh_extra = anggota_tubuh + ["tangan", "jari"]
print(anggota_tubuh_extra, "\n")  # Output: ['kepala', 'leher', 'bahu', 'lengan', 'mulut', 'kaki', 'tangan', 'jari']

# Removing list elements
del anggota_tubuh[0]
print(anggota_tubuh, "\n")  # Output: ['leher', 'bahu', 'lengan', 'mulut', 'kaki']

del anggota_tubuh_extra[2:4]
print(anggota_tubuh_extra, "\n")  # Output: ['kepala', 'leher', 'mulut', 'kaki', 'tangan', 'jari']

# Behind the scenes
x = ["a", "b", "c"]
y = x
y[1] = "z"
print("x: ", x)  # Output: ['a', 'z', 'c']
print("y: ", y, "\n")  # Output: ['a', 'z', 'c']

# Notes: x dan y merujuk ke list yang sama di memori. Perubahan pada y juga memengaruhi x.

# Jika ingin membuat salinan baru dari list, gunakan fungsi list() atau slicing.
x = ["a", "b", "c"]
y = list(x)  # Membuat salinan baru dari list x
y = x[:]     # Alternatif lain untuk membuat salinan baru
y[1] = "z"
print("x: ", x)  # Output: ['a', 'b', 'c']
print("y: ", y)  # Output: ['a', 'z', 'c']