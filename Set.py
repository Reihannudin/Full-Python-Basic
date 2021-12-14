"Set"
"""
Set digunakan untuk menyimpan beberapa item dalam satu variabel.
adalah kumpulan yang tidak berurutan, tidak dapat diubah*, dan tidak terindeks. Tidak ada anggota duplikat.
Himpunan adalah kumpulan yang unordered , unchangeable* , dan unindexed .

* Catatan: Set item yang tidak bisa diubah, tetapi Anda dapat menghapus item dan menambahkan item baru.

Himpunan ditulis dengan kurung kurawal.
"""
thisisset = {"appels", "bananas", "cherys"}
print(thisisset)

"""
Set Items
Item yang ditetapkan tidak berurutan, tidak dapat diubah, dan tidak mengizinkan nilai duplikat.
"""

"""
Unordered
Tidak berurutan berarti item dalam satu set tidak memiliki urutan yang ditentukan.
Item yang ditetapkan dapat muncul dalam urutan yang berbeda setiap kali Anda menggunakannya, dan tidak dapat dirujuk dengan indeks atau kunci.
"""

"""
Unchangeable
Item set tidak dapat diubah, artinya kita tidak dapat mengubah item setelah set dibuat.
Setelah kumpulan dibuat, Anda tidak dapat mengubah itemnya, tetapi Anda dapat menghapus item dan menambahkan item baru.
"""

"""
Duplicates Not Allowed
Set tidak boleh memiliki dua item dengan nilai yang sama.
"""
thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)

"""
Dapatkan Panjang Satu Set
Untuk menentukan berapa banyak item yang dimiliki satu set, gunakan len()metode.
"""
thisset = {"apple", "banana", "cherry"}

print(len(thisset))

""" Tetapkan Item - Tipe Data
Item yang disetel dapat berupa tipe data apa pun:"""
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

'Satu set dapat berisi tipe data yang berbeda:'
set1 = {"abc", 34, True, 40, "male"}

"""
Tipe()
Dari perspektif Python, set didefinisikan sebagai objek dengan tipe data 'set':
"""
myset = {"apple", "banana", "cherry"}
print(type(myset))

"""Set() Konstruktor
Dimungkinkan juga untuk menggunakan konstruktor set() untuk membuat set."""
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

# -------------------------------------------------
'Access Set Items'
"""
Akses Item
Anda tidak dapat mengakses item dalam kumpulan dengan mengacu pada indeks atau kunci.
Tetapi Anda dapat mengulang item yang disetel menggunakan for loop, 
"""
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

'atau menanyakan apakah nilai yang ditentukan ada dalam set, dengan menggunakan in kata kunci.'

thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)

"""
Ubah Item
Setelah set dibuat, Anda tidak dapat mengubah itemnya, tetapi Anda dapat menambahkan item baru.
"""
# ----------------------------------------------------

'Add Set Items'
"""
Setelah set dibuat, Anda tidak dapat mengubah itemnya, tetapi Anda dapat menambahkan item baru.
Untuk menambahkan satu item ke set gunakan add() metode.
"""
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

"""
Tambahkan Set
Untuk menambahkan item dari set lain ke set saat ini, gunakan update() metode.
"""
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

"""
Tambahkan Setiap Iterable
Objek dalam update()metode tidak harus berupa kumpulan, dapat berupa objek yang dapat diubah (tupel, daftar, kamus, dll.)
"""
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)

# -------------------------------------
"""
Remove Set Items
Untuk menghapus item dalam kumpulan, gunakan remove(), atau discard()metode
"""
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)

'Catatan: Jika item yang akan dihapus tidak ada, remove()akan memunculkan kesalahan.'
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)

""""
Catatan: Jika item yang akan dihapus tidak ada, TIDAK discard() akan menimbulkan kesalahan.
Anda juga dapat menggunakan pop() metode untuk menghapus item, tetapi metode ini akan menghapus item terakhir . Ingat bahwa set tidak berurutan, jadi Anda tidak akan tahu item apa yang dihapus.
Nilai kembalian pop()metode adalah item yang dihapus.
"""

thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)

'Catatan: Kumpulan tidak berurutan , jadi saat menggunakan pop()metode ini, Anda tidak tahu item mana yang dihapus.'
'The clear() Metode mengosongkan set:'

thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)

'Kata kunci del akan menghapus set sepenuhnya:'

thisset = {"apple", "banana", "cherry"}

del thisset

#print(thisset)

# ----------------------------------

'Loop Sets'
""" Anda dapat mengulang item yang disetel dengan menggunakan for loop:"""
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

# -----------------------------------------

'Join Sets'
""""
Gabung Dua Set
Ada beberapa cara untuk menggabungkan dua atau lebih set dengan Python.

Anda dapat menggunakan union()metode yang mengembalikan set baru yang berisi semua item dari kedua set,
atau update()metode yang menyisipkan semua item dari satu set ke set lainnya:
"""
'The union()method mengembalikan satu set baru dengan semua item dari kedua set:'
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

'The update()Metode memasukkan item dalam set2 ke set1'
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

'Catatan: Keduanya union()dan update() akan mengecualikan item duplikat apa pun.'

""" 
Simpan HANYA Duplikatnya
The intersection_update()Metode akan tetap hanya item yang hadir di kedua set.
"""
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)

'the intersection() Metode akan kembali baru ditetapkan, yang hanya berisi item yang hadir di kedua set.'

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)

"""
Simpan Semua, Tapi BUKAN Duplikatnya
The symmetric_difference_update()Metode akan tetap hanya elemen-elemen yang tidak hadir di kedua set.
"""
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)

'The symmetric_difference()Metode akan kembali satu set baru, yang hanya berisi elemen-elemen yang tidak hadir di kedua set.'
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

print(z)

# ----------------------------
'Set Methode'
""""
Method	                        Description
add()	                        Adds an element to the set
clear()	                        Removes all the elements from the set
copy()	                        Returns a copy of the set
difference()	                Returns a set containing the difference between two or more sets
difference_update()	            Removes the items in this set that are also included in another, specified set
discard()	                    Remove the specified item
intersection()     	            Returns a set, that is the intersection of two other sets
intersection_update()           Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	                Returns whether two sets have a intersection or not
issubset()        	            Returns whether another set contains this set or not
issuperset()	                Returns whether this set contains another set or not
pop()	                        Removes an element from the set
remove()	                    Removes the specified element
symmetric_difference()          Returns a set with the symmetric differences of two sets
symmetric_difference_update()	inserts the symmetric differences from this set and another
union()                        	Return a set containing the union of sets
update()	                    Update the set with the union of this set and others

"""