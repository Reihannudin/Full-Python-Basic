'Lambda'
"""
Fungsi lambda adalah fungsi anonim kecil.

Fungsi lambda dapat mengambil sejumlah argumen, tetapi hanya 
dapat memiliki satu ekspresi.
"""
'Sintaksis'
lambda arguments : 'expression'
'Ekspresi dieksekusi dan hasilnya dikembalikan'
x = lambda a : a + 10
print(x(5))

'Fungsi Lambda dapat mengambil sejumlah argumen:'
x = lambda a, b : a * b
print(x(5, 6))
# and
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

"""
Mengapa Menggunakan Fungsi Lambda?
Kekuatan lambda lebih baik ditampilkan saat Anda menggunakannya sebagai fungsi anonim di dalam fungsi lain.

Katakanlah Anda memiliki definisi fungsi yang mengambil satu argumen, dan argumen itu akan dikalikan dengan angka yang tidak dikenal:
"""

def myfunc (n):
    return lambda a : a * n

'Gunakan definisi fungsi itu untuk membuat fungsi yang selalu menggandakan nomor yang Anda kirim:'
mydoubler = myfunc(2)
print(mydoubler(11))

'Atau, gunakan definisi fungsi yang sama untuk membuat fungsi yang selalu melipatgandakan jumlah yang Anda kirim:'
mytripler = myfunc(3)
print(mytripler(11))

'Note : Gunakan fungsi lambda ketika fungsi anonim diperlukan untuk waktu yang singkat.'