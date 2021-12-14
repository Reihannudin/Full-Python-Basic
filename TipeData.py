"""
Tipe Data Python

Tipe Data Bawaan
Dalam pemrograman, tipe data merupakan konsep penting.

Variabel dapat menyimpan data dari tipe yang berbeda, dan tipe yang berbeda dapat melakukan hal yang berbeda.

Python memiliki tipe data berikut bawaan secara default, dalam kategori ini:

Jenis Teks:	str
Jenis numerik:	int, float, complex
Jenis Urutan:	list, tuple, range
Jenis Pemetaan:	dict
Setel Jenis:	set, frozenset
Tipe Boolean:	bool
Jenis Biner:	bytes, bytearray, memoryview
"""

# ------------------------------

"""
Mendapatkan Tipe Data
Anda bisa mendapatkan tipe data objek apa pun dengan menggunakan type()fungsi:
"""
x = 5
print(type(x))

""" Mengatur Tipe Data
Di Python, tipe data diatur saat Anda menetapkan nilai ke variabel:
"""
x = "Hello, Hello!!" #ini tipe data String (str)
x = 41 #ini tipe data Integer (int)
x = 41.91 #ini tipe data Float (Float)
x = 1j #ini tipe data Complex (complex)
x =  ["apple", "pisang", " semangka"] #ini tipe data List (list)
x =  ("apple", "pisang", " semangka") #ini tipe data Tuple (tuple)
x = range(7) #ini tipe data Range (range)
x =  {"name" : "Nadia", "age" : 16 } #ini tipe data Dict (dict)
x = {"apple", "pisang", " semangka"} #ini tipe data Set (set)
x =  frozenset({"apple", "pisang", " semangka"})#ini tipe data Frozenset (frozenset)
x =  True #ini tipe data Bool (bool)
x =  b"Hallo" #ini tipe data Bytes (bytes)
x =  bytearray(5)#ini tipe data ByteArray (bytearray)
x =  memoryview(bytes(9)) #ini tipe data MemoryView (memmoryview)

""" 
Mengatur Jenis Data Tertentu
Jika Anda ingin menentukan tipe data, Anda dapat menggunakan fungsi konstruktor berikut:
"""

x = str("Hello, Hello!!") #ini tipe data String (str)
x = int(41) #ini tipe data Integer (int)
x = float(41.91) #ini tipe data Float (Float)
x = complex(1j) #ini tipe data Complex (complex)
x = list(("apple", "pisang", " semangka")) #ini tipe data List (list)
x =  tuple(("apple", "pisang", " semangka")) #ini tipe data Tuple (tuple)
x = range(7) #ini tipe data Range (range)
x =  dict(name = "Nadia", age = 16) #ini tipe data Dict (dict)
x = set(("apple", "pisang", " semangka")) #ini tipe data Set (set)
x =  frozenset(("apple", "pisang", " semangka"))#ini tipe data Frozenset (frozenset)
x =  bool(42) #ini tipe data Bool (bool)
x =  bytes(5) #ini tipe data Bytes (bytes)
x =  bytearray(5)#ini tipe data ByteArray (bytearray)
x =  memoryview(bytes(9)) #ini tipe data MemoryView (memmoryview)

