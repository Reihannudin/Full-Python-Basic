'For loop'
"""
Sebuah for loop digunakan untuk iterasi berurutan (yang baik daftar, tupel, kamus, set, atau string).

Ini kurang seperti kata kunci for dalam bahasa pemrograman lain,
dan berfungsi lebih seperti metode iterator seperti yang ditemukan dalam bahasa pemrograman berorientasi objek lainnya.

Dengan for loop kita dapat mengeksekusi satu set pernyataan, sekali untuk setiap item dalam daftar, tuple, set dll.
"""
'Cetak setiap buah dalam daftar buah:'
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

'The for loop tidak memerlukan variabel pengindeksan untuk mengatur terlebih dahulu.'

"""
Looping Melalui String
Bahkan string adalah objek yang dapat diubah, mereka berisi urutan karakter:
"""
for x in "banana":
  print(x)

'Break Statment'
'Dengan pernyataan break, kita dapat menghentikan loop sebelum loop melewati semua item:'

'Keluar dari loop ketika x"pisang":'
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

'Keluar dari loop ketika x"pisang", tetapi kali ini jeda datang sebelum cetakan:'
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

'Countinue Statement'
'Dengan pernyataan continue kita dapat menghentikan iterasi loop saat ini, dan'
'melanjutkan dengan yang berikutnya:'
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

'The range() Function'
"""
Untuk mengulang satu set kode beberapa kali, kita dapat menggunakan fungsi range() ,
Fungsi range() mengembalikan urutan angka, mulai dari 0 secara default, dan bertambah 1
 (secara default), dan berakhir pada angka yang ditentukan.
"""
for x in range(9):
    print(x)

'Perhatikan bahwa rentang(6) bukanlah nilai 0 hingga 6, tetapi nilai 0 hingga 5.'

"""
Fungsi range() default ke 0 sebagai nilai awal, namun dimungkinkan untuk menentukan nilai awal
 dengan menambahkan parameter: range(2, 6) , yang berarti nilai dari 2 hingga 6 (tetapi tidak termasuk 6):
"""
for x in range(2, 6):
  print(x)

"""
Fungsi range() default untuk menambah urutan sebesar 1, namun dimungkinkan untuk menentukan nilai kenaikan
 dengan menambahkan parameter ketiga: range(2, 30, 3 ) :
"""
for x in range(2, 30, 3):
  print(x)

'Else in For Loop'
"""Kata elsekunci dalam forloop menentukan blok kode yang akan dieksekusi ketika loop selesai:"""
for x in range(6):
  print(x)
else:
  print("Finally finished!")

'Catatan: The elseblok TIDAK akan dieksekusi jika loop dihentikan oleh breakpernyataan.'
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")

'Loop Nested'
"""
Loop Nested adalah loop di dalam loop.

Loop dalam" akan dieksekusi satu kali untuk setiap iterasi "loop luar":
"""
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

'Pass Statement'
"""forloop tidak boleh kosong, tetapi jika Anda karena alasan tertentu memiliki
 forloop tanpa konten, masukkan passpernyataan untuk menghindari kesalahan.
 """
for x in [0, 1, 2]:
  pass