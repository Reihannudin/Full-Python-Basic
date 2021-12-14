"""
Kondisi Python dan pernyataan If
Python mendukung kondisi logis yang biasa dari matematika:

Sama dengan: a == b
Tidak Sama dengan: a != b
Kurang dari: a < b
Kurang dari atau sama dengan: a <= b
Lebih besar dari: a > b
Lebih besar dari atau sama dengan: a >= b
Kondisi ini dapat digunakan dalam beberapa cara, paling umum dalam "pernyataan if" dan loop.

Sebuah "pernyataan if" ditulis dengan menggunakan kata kunci if .
"""
a = 33
b = 200
if b > a:
  print("b is greater than a")
"""
Dalam contoh ini kita menggunakan dua variabel, a dan b , yang digunakan sebagai bagian dari
pernyataan if untuk menguji apakah b lebih besar dari a . Karena a adalah 33 , dan b adalah 200,
kita tahu bahwa 200 lebih besar dari 33, jadi kita mencetak ke layar bahwa "b lebih besar dari a".
"""

"Indentation"
"""  
Python bergantung pada lekukan (spasi putih di awal baris) untuk menentukan ruang lingkup dalam kode.
Bahasa pemrograman lain sering menggunakan kurung kurawal untuk tujuan ini.
"""
"""
a = 33
b = 200
if b > a:
print("b is greater than a") # you will get an error
"""

'Elif'
"""
Elif
Kata kunci elif adalah cara ular piton untuk mengatakan "jika kondisi sebelumnya tidak benar, maka coba kondisi ini".
"""
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
"""
Dalam contoh ini a sama dengan b , jadi kondisi pertama tidak benar, tetapi kondisi elif benar,
 jadi kami mencetak ke layar bahwa "a dan b sama".
"""

'Else'
"""
Else
Kata kunci else menangkap apa pun yang tidak ditangkap oleh kondisi sebelumnya.
"""
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
"""
Dalam contoh ini a lebih besar dari b , jadi kondisi pertama tidak benar, 
juga kondisi elif tidak benar, jadi kita pergi ke kondisi lain dan mencetak 
ke layar bahwa "a lebih besar dari b".

Anda juga dapat memiliki else tanpa elif:
"""
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

'Short Hand If'
"""
Jika Anda hanya memiliki satu pernyataan untuk dieksekusi, Anda dapat meletakkannya di baris
yang sama dengan pernyataan if.
"""
'Satu baris jika pernyataan:'
if a > b: print("a is greater than b")

'Short Hand If...Else'
"""
Jika Anda hanya memiliki satu pernyataan untuk dieksekusi, satu untuk jika, dan satu untuk yang lain,
Anda dapat meletakkan semuanya di baris yang sama:
"""
'Satu baris jika pernyataan lain:'
a =2
b = 70
print("A") if a > b else print("B")
'Teknik ini dikenal sebagai Ternary Operators , atau Conditional Expressions .'

"""
Anda juga dapat memiliki beberapa pernyataan lain pada baris yang sama:

Contoh
Satu baris pernyataan if else, dengan 3 kondisi:
"""
a = 300
b = 300
print("A") if a > b else print("=") if a == b else print("B") 

'And'
"""
Kata kunci and adalah operator logika, dan digunakan untuk menggabungkan pernyataan bersyarat:
"""
'Uji jika alebih besar dari b, DAN jika c lebih besar dari a:'
a = 200
b = 33
c = 190
if a > b and c > a:
  print("Both conditions are True")
elif a > b and c < a:
    print("just get once conditions")

'Or'
"""
Kata orkunci adalah operator logika, dan digunakan untuk menggabungkan pernyataan bersyarat:

Uji jika alebih besar dari b, ATAU jika a lebih besar dari c:
"""
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

'If Nested'
"""
Anda dapat memiliki ifpernyataan di dalam ifpernyataan, ini disebut pernyataan bersarang if .
"""
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

'The pass Statement'
"""
ifpernyataan tidak boleh kosong, tetapi jika Anda karena alasan tertentu memiliki ifpernyataan tanpa konten,
masukkan pass pernyataan tersebut untuk menghindari kesalahan.
"""
a = 33
b = 200

if b > a:
  pass