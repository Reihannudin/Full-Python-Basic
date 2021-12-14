'Python RegEx'
""""
RegEx, atau Ekspresi Reguler, adalah urutan karakter yang membentuk pola pencarian.

RegEx dapat digunakan untuk memeriksa apakah string berisi pola pencarian yang ditentukan.
"""
"""
Modul RegEx
Python memiliki paket bawaan yang disebut re, yang dapat digunakan untuk bekerja dengan Ekspresi Reguler.

Impor remodul:
"""
import re

"""
RegEx dengan Python
Setelah Anda mengimpor remodul, Anda dapat mulai menggunakan ekspresi reguler:
"""
'Cari string untuk melihat apakah itu dimulai dengan "The" dan diakhiri dengan "Spanyol":'

import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

'''
Fungsi RegEx
The reModul menawarkan satu set fungsi yang memungkinkan kita untuk mencari string untuk pertandingan:

Function	Description
findall	    Returns a list containing all matches
search	    Returns a Match object if there is a match anywhere in the string
split	    Returns a list where the string has been split at each match
sub     	Replaces one or many matches with a string
'''

'''
Fungsi findall()
The findall()fungsi mengembalikan daftar yang berisi semua pertandingan.
'''
import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

'''
Daftar tersebut berisi kecocokan dalam urutan mereka ditemukan.

Jika tidak ada kecocokan yang ditemukan, daftar kosong akan dikembalik
'''

'Kembalikan List kosong jika tidak ditemukan kecocokan:'
import re

txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)

'''
Fungsi pencarian ()
The search()fungsi pencarian string untuk pertandingan, dan mengembalikan objek Pertandingan jika ada pertandingan.

Jika ada lebih dari satu kecocokan, hanya kemunculan pertama kecocokan yang akan dikembalikan:
'''
'Cari karakter spasi putih pertama dalam string:'
import re

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())

'Jika tidak ada kecocokan yang ditemukan, nilai Noneakan dikembalikan:'
import re

txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)

'''
Pemisahan () Fungsi
The split()fungsi mengembalikan daftar di mana string telah perpecahan di setiap pertandingan:
'''
import re

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)

'Anda dapat mengontrol jumlah kemunculan dengan menentukan maxsplit parameter:'

import re

txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)

'''
Sub() Fungsi
The sub()Fungsi menggantikan pertandingan dengan teks pilihan Anda:
'''
'Ganti setiap karakter spasi putih dengan angka 9:'
import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)

'Anda dapat mengontrol jumlah penggantian dengan menentukan count parameter:'
import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)


""""
Cocokkan Obyek
Match Object adalah objek yang berisi informasi tentang pencarian dan hasilnya.

Catatan: Jika tidak ada yang cocok, nilai yang Noneakan dikembalikan, bukan Objek yang Cocok.

"""

'Lakukan pencarian yang akan mengembalikan Objek yang Cocok:'

import re

txt = "The rain in Spain"
x = re.search("ai", txt)
print(x) #this will print an object

'''
Objek Match memiliki properti dan metode yang digunakan untuk mengambil informasi tentang pencarian, dan hasilnya:

.span()mengembalikan Tuple yang berisi posisi awal, dan akhir pertandingan.
.stringmengembalikan string yang diteruskan ke fungsi
.group()mengembalikan bagian string yang cocok
'''

'''
Cetak posisi (posisi awal dan akhir) dari kejadian kecocokan pertama.

Ekspresi reguler mencari kata apa pun yang dimulai dengan huruf besar "S":
'''
import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())

'Cetak string yang diteruskan ke fungsi:'
import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)

'''
Cetak bagian string di mana ada kecocokan.

Ekspresi reguler mencari kata apa pun yang dimulai dengan huruf besar "S":
'''
import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())

'Catatan: Jika tidak ada yang cocok, nilai yang Noneakan dikembalikan, bukan Objek yang Cocok.'