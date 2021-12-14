"""
Modul Python
Apa itu Modul?
Anggap sebuah modul sama dengan pustaka kode.

File yang berisi sekumpulan fungsi yang ingin Anda sertakan dalam aplikasi Anda.
"""
"""
Gunakan Modul
Sekarang kita dapat menggunakan modul yang baru saja kita buat, dengan menggunakan importpernyataan:
"""
import mymodule

mymodule.greeting("Jonathan")

"""
Catatan: Saat menggunakan fungsi dari modul, gunakan sintaks: module_name.function_name .

Variabel dalam Modul
Modul dapat berisi fungsi, seperti yang telah dijelaskan, tetapi juga variabel dari semua jenis (array, kamus, objek, dll):

Impor modul bernama mymodule, dan akses kamus person1:

"""
import mymodule

a = mymodule.person1["age"]
print(a)

"""
Menamai Modul
Anda dapat memberi nama file modul apa pun yang Anda suka, tetapi harus memiliki ekstensi file .py

Menamai Ulang Modul
Anda dapat membuat alias saat mengimpor modul, dengan menggunakan askata kunci

Buat alias untuk mymoduledisebut mx:
"""
import mymodule as mx

a = mx.person1["age"]
print(a)


"""
Modul bawaan
Ada beberapa modul bawaan dalam Python, yang dapat Anda impor kapan pun Anda mau.
"""

'Impor dan gunakan platformmodul:'

import platform

x = platform.system()
print(x)

"""
Menggunakan Fungsi dir()
Ada fungsi bawaan untuk mendaftar semua nama fungsi (atau nama variabel) dalam sebuah modul. The dir()Fungsi:


Daftar semua nama yang ditentukan milik modul platform:
"""
import platform

x = dir(platform)
print(x)

"""
Catatan: Fungsi dir() dapat digunakan pada semua modul, juga yang Anda buat sendiri.

Impor Dari Modul
Anda dapat memilih untuk mengimpor hanya bagian dari modul, dengan menggunakan fromkata kunci.
"""
'Modul bernama mymodulememiliki satu fungsi dan satu kamus:'

from mymodule import person1

print (person1["age"])

"""Catatan: Saat mengimpor menggunakan from kata kunci, jangan gunakan nama modul saat merujuk ke elemen dalam modul.
 Contoh: person1["age"], bukan mymodule.person1["age"]"""