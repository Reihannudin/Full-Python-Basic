"""
Kelas/Objek Python
Python adalah bahasa pemrograman berorientasi objek.

Hampir semua yang ada di Python adalah objek, dengan properti dan metodenya.

Kelas seperti konstruktor objek, atau "cetak biru" untuk membuat objek.
"""

""""
Buat Kelas
Untuk membuat kelas, gunakan kata kunci class:
"""
class MyClass:
  x = 5

"""
Buat Objek
Sekarang kita dapat menggunakan kelas bernama MyClass untuk membuat objek:
"""
p1 = MyClass()
print(p1.x)

"""
Fungsi __init__()
Contoh di atas adalah kelas dan objek dalam bentuknya yang paling sederhana,
 dan tidak terlalu berguna dalam aplikasi kehidupan nyata.

Untuk memahami arti kelas, kita harus memahami fungsi __init__() bawaan.

Semua kelas memiliki fungsi yang disebut __init__(), yang selalu dijalankan ketika kelas sedang dimulai.

Gunakan fungsi __init__() untuk menetapkan nilai ke properti objek, 
atau operasi lain yang perlu dilakukan saat objek sedang dibuat:
"""
class Person: 
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
p1 = Person("Nadia", 16)

print(p1.name)
print(p1.age)

""" Catatan: The __init__()fungsi disebut secara otomatis setiap kali 
kelas sedang digunakan untuk membuat objek baru."""


"""
Metode Objek
Objek juga dapat berisi metode. Metode dalam objek adalah fungsi yang dimiliki objek.

Mari kita membuat metode di kelas Person:
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def myfunc(self):
        print("Hello my name is " + self.name)

p1 = Person("Nadia", 16)
p1.myfunc()

"""
Catatan: The self parameter adalah referensi ke contoh saat ini kelas, dan digunakan untuk variabel akses dalam kelas.
"""

"""
Parameter diri sendiri
The selfparameter adalah referensi ke contoh saat ini kelas, dan digunakan untuk variabel akses yang dimiliki kelas.

Itu tidak harus bernama self, Anda dapat menyebutnya apa pun yang Anda suka, tetapi itu harus menjadi 
parameter pertama dari fungsi apa pun di kelas:
"""
class Person:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age
    
    def myfunc(abc):
        print("Hello my name is " + abc.name)

p1 = Person("Fairis", 15)
p1.myfunc()

"""
Ubah Properti Objek
Anda dapat memodifikasi properti pada objek seperti ini:
"""
p1.age = 20

"""
Hapus Properti Objek
Anda dapat menghapus properti pada objek dengan menggunakan delkata kunci:
"""
del p1.age

"""
Hapus Objek
Anda dapat menghapus objek dengan menggunakan delkata kunci:
"""
del p1

""" 
Pass Statement
classdefinisi tidak boleh kosong, tetapi jika Anda karena alasan tertentu 
memiliki classdefinisi tanpa konten, masukkan passpernyataan untuk menghindari kesalahan.
"""
class Person:
    pass

