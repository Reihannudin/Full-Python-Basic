"""
Python Iterator
Iterator adalah objek yang berisi sejumlah nilai yang dapat dihitung.

Iterator adalah objek yang dapat diulang, artinya Anda dapat melintasi semua nilai.

Secara teknis, dalam Python, iterator adalah objek yang mengimplementasikan protokol iterator,
 yang terdiri dari metode __iter__() dan __next__().
"""

"""
Iterator vs Iterable
List, tupel, Dictonary, dan set semuanya adalah objek yang dapat diubah.
 Mereka adalah wadah yang dapat diubah tempat Anda bisa mendapatkan iterator.

Semua objek ini memiliki iter()metode yang digunakan untuk mendapatkan iterator:
"""
'Kembalikan iterator dari Tuple, dan cetak setiap nilai:'
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

'Bahkan string adalah objek yang dapat diubah, dan dapat mengembalikan iterator:'
mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

""""
Looping Melalui Iterator
Kami juga dapat menggunakan forloop untuk beralih melalui objek yang dapat diubah:
"""
'Iterasi nilai tuple:'
mytuple = ("apple", "banana", "cherry")

for x in mytuple:
  print(x)


'Iterasi karakter string:'
mystr = "nadia"

for x in mystr:
  print(x)

"""
The forLoop benar-benar menciptakan sebuah objek iterator dan mengeksekusi ()
 metode berikutnya untuk setiap loop.
"""


""""
Buat Iterator
Untuk membuat objek/kelas sebagai iterator, 
Anda harus mengimplementasikan metode __iter__() dan __next__() ke objek Anda.

Seperti yang telah Anda pelajari di bab Python Classes/Objects ,
semua kelas memiliki fungsi yang disebut __init__(), 
yang memungkinkan Anda melakukan inisialisasi saat objek sedang dibuat.

The __iter__()Metode bertindak serupa, Anda dapat melakukan operasi (menginisialisasi dll),
tetapi harus selalu kembali objek iterator sendiri.

The __next__()Metode ini juga memungkinkan Anda untuk melakukan operasi,
dan harus kembali item berikutnya dalam urutan.
"""

"""
Contoh
Buat iterator yang mengembalikan angka, dimulai dengan 1, 
dan setiap urutan akan bertambah satu 
(mengembalikan 1,2,3,4,5 dll.):
"""
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x

MyClass = MyNumbers()
MyIter = iter(MyClass)

print(next(MyIter))
print(next(MyIter))
print(next(MyIter))
print(next(MyIter))
print(next(MyIter))
print(next(MyIter))

"""
StopIteration
Contoh di atas akan berlanjut selamanya jika Anda memiliki cukup pernyataan next(),
 atau jika digunakan dalam satu forlingkaran.

Untuk mencegah iterasi berlangsung selamanya, kita dapat menggunakan 
StopIterationpernyataan.

Dalam __next__()metode ini, kita dapat menambahkan kondisi terminasi untuk memunculkan
 kesalahan jika iterasi dilakukan beberapa kali:
"""

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
 print(x)
