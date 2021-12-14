"""Daftar
Daftar adalah kumpulan yang tersusun dan dapat diubah-ubah. Memungkinkan anggota duplikat.
Daftar digunakan untuk menyimpan beberapa item dalam satu variabel.
Daftar adalah salah satu dari 4 tipe data bawaan dalam Python yang digunakan untuk menyimpan koleksi data, 3 lainnya adalah Tuple , Set , dan Dictionary , semuanya dengan kualitas dan penggunaan yang berbeda.
Daftar dibuat menggunakan tanda kurung siku:"""

belanjaan = ['kebab', 'bakso', 'mie instant']
print(belanjaan)

"""List Items
list items diurutkan, dapat diubah, dan memungkinkan nilai duplikat.

Daftar item diindeks, item pertama memiliki indeks [0], item kedua memiliki indeks, [1]dll."""

"""Ordered 
Ketika kita mengatakan bahwa daftar diurutkan, itu berarti item memiliki urutan yang ditentukan, dan urutan itu tidak akan berubah.

Jika Anda menambahkan item baru ke daftar, item baru akan ditempatkan di akhir daftar."""

""" Changeable
 Daftar tersebut dapat diubah, artinya kita dapat mengubah, menambah, dan menghapus item dalam daftar setelah dibuat."""


"""Allow Duplicates 
Karena daftar diindeks, daftar dapat memiliki item dengan nilai yang sama"""
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

"""List Length
Untuk menentukan berapa banyak item yang dimiliki daftar, gunakan len()fungsi:"""
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

"""List Items - Data Types
Item daftar dapat berupa tipe data apa pun:"""
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
# Daftar dapat berisi tipe data yang berbeda
list1 = ["abc", 34, True, 40, "male"]

"""type()"""
mylist = ["apple", "banana", "cherry"]
print(type(mylist))

""" The list() Constructor 
Dimungkinkan juga untuk menggunakan konstruktor list() saat membuat daftar baru.
"""

# ----------------------------------
"""Access List Items
Daftar item diindeks dan Anda dapat mengaksesnya dengan mengacu pada nomor indeks:
"""
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

"""
Pengindeksan Negatif
Pengindeksan negatif berarti mulai dari akhir
-1 mengacu pada item terakhir, -2 mengacu pada item terakhir kedua dll."""

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

"""
Rentang Indeks
Anda dapat menentukan rentang indeks dengan menentukan di mana harus memulai dan di mana harus mengakhiri rentang.

Saat menentukan rentang, nilai yang dikembalikan akan menjadi daftar baru dengan item yang ditentukan.
"""
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

"""
Dengan mengabaikan nilai awal, rentang akan dimulai pada item pertama:
"""
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

"""
Dengan mengabaikan nilai akhir, rentang akan berlanjut ke akhir daftar:
"""
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

"""Rentang Indeks Negatif
Tentukan indeks negatif jika Anda ingin memulai pencarian dari akhir daftar:"""
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

"""Periksa apakah Barang Ada
Untuk menentukan apakah item tertentu ada dalam daftar, gunakan inkata kunci:"""
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")


#   ---------------------------------------------
"""Change List Items"""

"""Ubah Nilai Barang
Untuk mengubah nilai item tertentu, lihat nomor indeks:"""
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

"""Ubah Rentang Nilai Item
Untuk mengubah nilai item dalam rentang tertentu, tentukan daftar dengan nilai baru,
dan rujuk ke rentang nomor indeks tempat Anda ingin menyisipkan nilai baru:"""
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

"""Jika Anda memasukkan lebih banyak item daripada yang Anda ganti, item baru akan disisipkan di tempat yang Anda tentukan,
 dan item yang tersisa akan bergerak sesuai:"""
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)


# ---------------------------------------------
"""Tambahkan Item
Untuk menambahkan item ke akhir daftar, gunakan metode append() """
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)


"""Sisipkan Item
Untuk menyisipkan item daftar pada indeks tertentu, gunakan insert()metode.
The insert()Metode menyisipkan item pada indeks tertentu:"""
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

"""Perpanjang Daftar
Untuk menambahkan elemen dari daftar lain ke daftar saat ini, gunakan extend()metode."""
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

"""Tambahkan Setiap Iterable
The extend()Metode tidak harus append daftar , Anda dapat menambahkan objek iterable (tupel, set, kamus dll)."""
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

# -----------------------------------------------
"Hapus Item Daftar"
"""Hapus Item Tertentu
The remove()Metode menghilangkan item tertentu."""
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

"""Hapus Indeks Tertentu
The pop()Metode menghilangkan indeks tertentu."""
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
'Jika Anda tidak menentukan indeks, pop()metode akan menghapus item terakhir.'

'Kata kunci del juga menghapus indeks yang ditentukan:'
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

'Kata delkunci juga dapat menghapus List sepenuhnya.'
thislist = ["apple", "banana", "cherry"]
del thislist

"""Hapus Daftar
The clear()Metode mengosongkan daftar.

Daftar itu masih ada, tetapi tidak ada isinya."""
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

# ----------------------------------------
""" Loop Lists"""
'Anda dapat mengulang item daftar dengan menggunakan for loop:'
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

  """Ulangi Nomor Indeks
Anda juga dapat mengulang item daftar dengan mengacu pada nomor indeksnya.
Gunakan fungsi range()and len()untuk membuat iterable yang sesuai."""
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

'Using a While Loop'
"""Anda dapat mengulang item daftar dengan menggunakan whileloop.
Gunakan len()fungsi untuk menentukan panjang daftar, lalu mulai dari 0 dan ulangi item daftar dengan mengacu pada indeksnya.
Ingatlah untuk meningkatkan indeks sebesar 1 setelah setiap"""
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

"""Perulangan Menggunakan Pemahaman Daftar
List Comprehension menawarkan sintaks terpendek untuk mengulang daftar:"""
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

"""List Comprehension
Pemahaman daftar menawarkan sintaks yang lebih pendek saat Anda ingin membuat daftar baru berdasarkan nilai dari daftar yang sudah ada.

Contoh:
Berdasarkan daftar buah-buahan, Anda menginginkan daftar baru, yang hanya berisi buah-buahan dengan huruf "a" pada namanya.
Tanpa pemahaman daftar, Anda harus menulis forpernyataan dengan tes bersyarat di dalamnya:"""
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

"""Sintaks
newlist = [expression for item in iterable if condition == True]
Nilai yang dikembalikan adalah daftar baru, membiarkan daftar lama tidak berubah."""

"""Kondisi
The kondisi seperti filter yang hanya menerima item yang valuate ke True."""
newlist1 = [x for x in fruits if x != "apple"]
print(newlist1)

"""iterable
The iterable dapat berupa objek iterable, seperti daftar, tuple, set dll

Contoh
Anda dapat menggunakan range()fungsi untuk membuat iterable:"""

newlist2 = [x for x in range(10)]
print(newlist2)

'Contoh yang sama, tetapi dengan condition:'
newlist3 = [x for x in range(10) if x < 5]
print(newlist3)


"""Ekspresi
The ekspresi adalah item saat ini di iterasi, tetapi juga hasil,
yang dapat Anda memanipulasi sebelum berakhir seperti daftar item dalam daftar baru:"""

newlist = [x.upper() for x in fruits]
print(newlist)

'Anda dapat mengatur hasilnya ke apa pun yang Anda suka:'
newlist = ['hello' for x in fruits]
print(newlist)

'The ekspresi juga dapat berisi kondisi, tidak seperti filter, tetapi sebagai cara untuk memanipulasi hasilnya:'
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)

# ---------------------------
'Sort Lists'
"""Urutkan Daftar Secara Alfanumerik
Objek daftar memiliki sort()metode yang akan mengurutkan daftar secara alfanumerik, menaik, secara default:"""

'urutan berdasarkan abjad'
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

'urutan berdasarkan numerik'
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

"""Urutan Desending
Untuk mengurutkan secara menurun, gunakan argumen kata kunci reverse = True:"""
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)


"""Sesuaikan Fungsi Sortir
Anda juga dapat menyesuaikan fungsi Anda sendiri dengan menggunakan argumen kata kunci .key = function

Fungsi akan mengembalikan angka yang akan digunakan untuk mengurutkan daftar (angka terendah terlebih dahulu):"""
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

"""Sortir Tidak Peka Huruf Besar-kecil
Secara default, sort()metode ini peka terhadap huruf besar-kecil, sehingga semua huruf kapital diurutkan sebelum huruf kecil:"""
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

"""Untungnya kita dapat menggunakan fungsi bawaan sebagai fungsi utama saat menyortir daftar.
Jadi jika Anda menginginkan fungsi pengurutan case-insensitive, gunakan str.lower sebagai fungsi kunci:"""
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

"""Urutan terbalik
Bagaimana jika Anda ingin membalik urutan daftar, terlepas dari alfabetnya?

The reverse()Metode membalikkan urutan penyortiran saat elemen."""
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

# --------------------------------------------------
'Copy Lists'

"""Copy list
Anda tidak dapat menyalin daftar hanya dengan mengetik list2 = list1, karena: list2hanya akan menjadi referensi ke list1, 
dan perubahan yang dibuat list1secara otomatis juga akan dibuat di list2.
Ada cara untuk membuat salinan, salah satu caranya adalah dengan menggunakan metode Daftar bawaan copy()."""
thislist = ["apple", "banana", "cherry", 'pepaya']
mylist = thislist.copy()
print(mylist)

'Cara lain untuk membuat salinan adalah dengan menggunakan metode bawaan list().'
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

# Join List
"""Join Two Lists
Ada beberapa cara untuk menggabungkan, atau menggabungkan, dua atau lebih daftar dengan Python.
Salah satu cara termudah adalah dengan menggunakan + operator."""
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

'Cara lain untuk menggabungkan dua daftar adalah dengan menambahkan semua item dari list2 ke dalam list1, satu per satu:'
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)
print(list1)

'Atau Anda dapat menggunakan extend() metode, yang tujuannya adalah untuk menambahkan elemen dari satu daftar ke daftar lain:'
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

# ------------------------------------------------
'List Methode'
"""
Method	    Description
append()	Menambahkan elemen di akhir list
clear()	    Menghapus semua elemen dari list
copy()      Mengembalikan salinan list
count()	    Mengembalikan jumlah elemen dengan nilai yang ditentukan
extend()	Tambahkan elemen list (atau iterable apa pun), ke akhir list saat ini
index()	    Mengembalikan indeks elemen pertama dengan nilai yang ditentukan
insert()	Menambahkan elemen pada posisi yang ditentukan
pop()	    Menghapus elemen pada posisi yang ditentukan
remove()	Menghapus item dengan nilai yang ditentukan
reverse()	Membalikkan urutan list
sort()   	Urutkan list
"""