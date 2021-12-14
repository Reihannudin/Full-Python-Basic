"""
Dictonary
Dictonary digunakan untuk menyimpan nilai data dalam pasangan kunci:nilai.

Dictonary adalah kumpulan yang ordered*, changeable and do not allow duplicates.

Pada Python versi 3.7, kamus dipesan . Di Python 3.6 dan sebelumnya, dictonary tidak berurutan .

Dictonary ditulis dengan kurung kurawal, dan memiliki kunci dan nilai:
"""
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

"""
Dictonary Item
Dictonary Item dapat di urutkan, dapat diubah, dan tidak mengizinkan duplikat.

Item kamus disajikan dalam pasangan kunci:nilai, dan dapat dirujuk dengan menggunakan nama kunci.
"""

"""
Diurutkan atau Tidak Diurutkan?
Pada Python versi 3.7, kamus dipesan . Di Python 3.6 dan sebelumnya, kamus tidak berurutan .

Ketika kita mengatakan bahwa dictonary, itu berarti item memiliki urutan yang ditentukan, dan urutan itu tidak akan berubah.

Tidak berurutan berarti item tidak memiliki urutan yang ditentukan, Anda tidak dapat merujuk ke item dengan menggunakan indeks.
"""

"""
Dapat diubah
Kamus dapat diubah, artinya kita dapat mengubah, menambah, atau menghapus item setelah kamus dibuat.
"""

"""
Duplikat Tidak Diizinkan
Kamus tidak boleh memiliki dua item dengan kunci yang sama:
"""
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

"""
Panjang kamus
Untuk menentukan berapa banyak item yang dimiliki kamus, gunakan len()fungsi:
"""
print(len(thisdict))

"""
Item Kamus - Tipe Data
Nilai dalam item kamus dapat berupa tipe data apa pun:
"""
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

"""
Tipe()
Dari perspektif Python, kamus didefinisikan sebagai objek dengan tipe data 'dict':
"""
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))

# ----------------------------
''' Mengakses Item
Anda dapat mengakses item kamus dengan mengacu pada nama kuncinya, di dalam tanda kurung siku:'''

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x)

'''Ada juga metode yang disebut get()yang akan memberi Anda hasil yang sama:'''
x = thisdict.get("model")
print(x)

'''Dapatkan Kunci
The keys()metode akan mengembalikan daftar semua kunci dalam kamus'''
x = thisdict.keys()
print(x)

'''Daftar kunci adalah tampilan kamus, artinya setiap perubahan yang dilakukan pada kamus akan tercermin dalam daftar kunci.'''

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change


# ------------------------------------\

'Change the item dictonary'
''''
Ubah Nilai
Anda dapat mengubah nilai item tertentu dengan mengacu pada nama kuncinya:
'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018
print(thisdict)

'''Perbarui Kamus
The update()Metode akan memperbarui kamus dengan item dari argumen yang diberikan.

Argumen harus berupa kamus, atau objek yang dapat diubah dengan pasangan kunci:nilai.'''

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})
print(thisdict)

# ------------------------------------\
'Remove the items'
'''
Menghapus Item
Ada beberapa metode untuk menghapus item dari kamus:
'''
'The pop()Metode menghilangkan item dengan nama kunci yang ditentukan:'

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

'The popitem()Metode menghilangkan item dimasukkan terakhir (dalam versi sebelum 3.7, item acak dihapus sebagai gantinya):'

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)

'Kata delkunci menghapus item dengan nama kunci yang ditentukan:'

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)

'Kata delkunci juga dapat menghapus kamus sepenuhnya:'

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict
#print(thisdict) #this will cause an error because "thisdict" no longer exists.

'The clear()Metode mengosongkan kamus:'

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)

# ---------------------------------------

'''
Dictonary Loop
Dictonary Loop
Anda dapat mengulang kamus dengan menggunakan forloop.

Saat mengulang melalui kamus, nilai yang dikembalikan adalah kunci dari kamus, tetapi ada juga metode untuk mengembalikan nilai .
'''
for x in thisdict:
  print(x)

'Cetak semua nilai dalam kamus, satu per satu:'
for x in thisdict:
  print(thisdict[x])

'Anda juga dapat menggunakan values()metode untuk mengembalikan nilai kamus:'
for x in thisdict.values():
  print(x)

'anda dapat menggunakan keys()metode untuk mengembalikan kunci kamus:'
for x in thisdict.keys():
  print(x)

'Ulangi kunci dan nilai , dengan menggunakan items()metode:'
for x, y in thisdict.items():
  print(x, y)

# -----------------------------------------
'''
Copy Dictionaries
Anda tidak dapat menyalin kamus hanya dengan mengetik dict2 = dict1, karena: dict2hanya akan menjadi referensi ke dict1, dan perubahan yang dibuat dict1secara otomatis juga akan dibuat di dict2.

Ada cara untuk membuat salinan, salah satu caranya adalah dengan menggunakan metode Kamus bawaan copy().
'''
'Buat salinan kamus dengan copy()metode:'

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

'Cara lain untuk membuat salinan adalah dengan menggunakan fungsi bawaan dict().'

'Buat salinan kamus dengan dict() fungsi:'

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)

# ------------------------------------\
'Nested Dictionaries'
"""
Kamus Bersarang
Kamus dapat berisi kamus, ini disebut kamus bersarang.
"""
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

'Atau, jika Anda ingin menambahkan tiga kamus ke dalam kamus baru:'

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(myfamily)

# ----------------------------------------------
'Dictonary Methode'
"""
Metode Kamus
Python memiliki seperangkat metode bawaan yang dapat Anda gunakan di kamus.

Method	        Description
clear()	        Removes all the elements from the dictionary
copy()	        Returns a copy of the dictionary
fromkeys()     	Returns a dictionary with the specified keys and value
get()	        Returns the value of the specified key
items()	        Returns a list containing a tuple for each key value pair
keys()	        Returns a list containing the dictionary's keys
pop()	        Removes the element with the specified key
popitem()	    Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	    Updates the dictionary with the specified key-value pairs
values()	    Returns a list of all the values in the dictionary
"""