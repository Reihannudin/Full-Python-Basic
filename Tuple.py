'Tuple Python'

"""
-Tuple
Tuple adalah koleksi yang dipesan dan tidak dapat diubah .
Tuple digunakan untuk menyimpan beberapa item dalam satu variabel.
Tuple adalah salah satu dari 4 tipe data bawaan dalam Python yang digunakan untuk menyimpan kumpulan data,
3 lainnya adalah List , Set , dan Dictionary , semuanya dengan kualitas dan penggunaan yang berbeda.

Tuple ditulis dengan tanda kurung bulat.
"""
thistuple = ("apple", "banana", "cherry")
print(thistuple)

"""
Item Tuple
Item tuple dipesan, tidak dapat diubah, dan memungkinkan nilai duplikat.

Item tupel diindeks, item pertama memiliki index [0], item kedua memiliki indeks [1]dll.
"""

"""
Ordered
Ketika kita mengatakan bahwa tupel dipesan, itu berarti item memiliki urutan yang ditentukan,
 dan urutan itu tidak akan berubah.
"""

"""
Unchangeable
Tuple tidak dapat diubah, artinya kita tidak dapat mengubah, menambah, atau menghapus item setelah tuple dibuat.
"""

"""
Allow Duplicates
Karena tupel diindeks, mereka dapat memiliki item dengan nilai yang sama:
"""
'contoh Tuple duplikat'
thisTuple = ("apple","banana","watermelon","banana", "apple")
print(thisTuple)

"""
Tuple Length
Untuk menentukan berapa banyak item yang dimiliki sebuah tuple, gunakan len()fungsi:
"""
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

"""
Tipe()
Dari perspektif Python, tupel didefinisikan sebagai objek dengan tipe data 'tuple':
"""
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))


"""
Buat Tuple Dengan Satu Item
Untuk membuat Tuple dengan hanya satu item, Anda harus menambahkan koma setelah item,
jika tidak Python tidak akan mengenalinya sebagai Tuple.
"""
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

"""
Item Tuple - Tipe Data
Item tuple dapat berupa tipe data apa pun:
"""
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
print(tuple1)
print(tuple2)
print(tuple3)

'Tuple dapat berisi tipe data yang berbeda:'
tuple1 = ("Nadia", 41, True, 3.000 , "Han")
print(tuple1)

"""
Tuple() Konstruktor
Dimungkinkan juga untuk menggunakan konstruktor Tuple() untuk membuat Tuple.
"""
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

# ---------------------------------------------

"""
Akses Item Tuple

Anda dapat mengakses item Tuple dengan mengacu pada nomor indeks, di dalam tanda kurung siku:
"""
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

"""
Pengindeksan Negatif
Pengindeksan negatif berarti mulai dari akhir.

-1 mengacu pada item terakhir, -2 mengacu pada item terakhir kedua dll.
"""
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

"""
Rentang Indeks
Anda dapat menentukan rentang indeks dengan menentukan di mana harus memulai dan di mana harus mengakhiri rentang.

Saat menentukan rentang, nilai yang dikembalikan akan menjadi tupel baru dengan item yang ditentukan.
"""
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

'Dengan mengabaikan nilai awal, rentang akan dimulai pada item pertama:'
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])

'Dengan mengabaikan nilai akhir, rentang akan berlanjut ke akhir daftar:'
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])

"""
Rentang Indeks Negatif
Tentukan indeks negatif jika Anda ingin memulai pencarian dari akhir Tuple:
"""
thistuple = ("apple","banana","cherry","orange", "kiwi","melon","mango")
print(thistuple)

"""
Periksa apakah Barang Ada
Untuk menentukan apakah item tertentu ada dalam tuple, gunakan inkata kunci:
"""
thistuple = ("apple", "banana", "cherry")
if "Nadia" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")
else: 
    print("tidak ada disini")

#---------------------------------------------------------- 

'Update Tuples'
"""
Ubah Nilai Tuple
Setelah tuple dibuat, Anda tidak dapat mengubah nilainya. Tuple tidak dapat diubah , atau tidak dapat diubah seperti yang juga disebut.

Tapi ada solusi. Anda dapat mengonversi Tuple menjadi daftar, mengubah daftar, dan mengonversi daftar kembali menjadi Tuple.
"""
x = ("apple", "banana","cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

"""
Tambahkan Item
Karena tupel tidak dapat diubah, mereka tidak memiliki append()metode bawaan, tetapi ada cara lain untuk menambahkan item ke tupel.

1. Convert into a list : Sama seperti solusi untuk mengubah tuple, Anda dapat mengubahnya menjadi daftar,
 menambahkan item Anda, dan mengubahnya kembali menjadi tuple.
"""
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

""" 
2. Tambahkan tupel ke tupel . Anda diperbolehkan untuk menambahkan tupel ke tupel, jadi jika Anda ingin menambahkan satu item, (atau banyak),
 buat tupel baru dengan item tersebut, dan tambahkan ke tupel yang ada:
"""
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)


""""
Hapus Item
Catatan: Anda tidak dapat menghapus item dalam Tuple.

Tuple tidak dapat diubah , jadi Anda tidak dapat menghapus item darinya,
tetapi Anda dapat menggunakan solusi yang sama seperti yang kami gunakan untuk mengubah dan menambahkan item Tuple:
"""
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

'Atau Anda dapat menghapus Tuple sepenuhnya:'
'Kata delkunci dapat menghapus Tuple sepenuhnya:'

thistuple = ("apple", "banana", "cherry")
del thistuple
#print(thistuple) #this will raise an error because the tuple no longer exists


# ----------------------------------------------------

'Unpack Tuples'
""""
Ketika kita membuat sebuah tuple, kita biasanya memberikan nilai padanya. Ini disebut "mengemas" sebuah tuple:
"""
'mengemas tuple'
fruits = ("apple", "banana", "cherry")

""" Namun, dalam Python, kita juga diperbolehkan untuk mengekstrak nilai kembali ke dalam variabel. 
Ini disebut "membongkar": """
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

"""Catatan: Jumlah variabel harus sesuai dengan jumlah nilai dalam tupel, jika tidak,
 Anda harus menggunakan tanda bintang untuk mengumpulkan nilai yang tersisa sebagai daftar."""


"""  Menggunakan Asterisk
Jika jumlah variabel kurang dari jumlah nilai, Anda dapat menambahkan an *ke nama variabel dan nilai akan ditetapkan ke variabel sebagai daftar:
"""
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

"""
Jika tanda bintang ditambahkan ke nama variabel lain selain yang terakhir,
Python akan memberikan nilai ke variabel hingga jumlah nilai yang tersisa cocok dengan jumlah variabel yang tersisa.
"""
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

# --------------------------------------------

'Loop Tuples'

'Loop Melalui Tuple'
'Anda dapat mengulang item Tuple dengan menggunakan forloop.'
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

"""
Ulangi Nomor Indeks
Anda juga dapat mengulang item Tuple dengan mengacu pada nomor indeksnya.
Gunakan fungsi range() and len() untuk membuat iterable yang sesuai."""

thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

""" 
Menggunakan Perulangan Sementara
Anda dapat mengulang item daftar dengan menggunakan whileloop.
Gunakan len()fungsi untuk menentukan panjang tupel, lalu mulai dari 0 dan ulangi item tupel dengan mengacu pada indeksnya.
Ingatlah untuk meningkatkan indeks sebesar 1 setelah setiap iterasi.
"""
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1

# -----------------------------------------
"""
Join Two Tuples
Untuk menggabungkan dua atau lebih tupel, Anda dapat menggunakan + operator:
"""
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

""" 
Kalikan Tuple
Jika Anda ingin mengalikan konten Tuple beberapa kali, Anda dapat menggunakan * operator:
"""
fruits = ("apples", "bananas", "cherrys")
mytuple = fruits * 2

print(mytuple)

# Metode Tuple
"""
Method	Description
count()	Mengembalikan berapa kali nilai tertentu muncul dalam sebuah tuple
index()	Mencari tuple untuk nilai yang ditentukan dan mengembalikan posisi di mana ia ditemukan
"""