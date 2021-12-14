"""
Tipe data Number pada Python
Ada tiga tipe numerik dalam Python:
int
float
complex
Variabel tipe numerik dibuat saat Anda menetapkan nilai padanya:
"""
a = 1    # int
b = 2.8  # float
c = 1j   # complex

# Untuk memverifikasi jenis objek apa pun dengan Python, gunakan type()fungsi:

print(type(a))
print(type(b))
print(type(c))

# ------------------------------

""" 
INT
Int, atau bilangan bulat, adalah bilangan bulat, positif atau negatif, tanpa desimal, dengan panjang tak terbatas.
"""

d = 1
f = 35656222554887711
g = -3255522

print(type(d))
print(type(f))
print(type(g))

# ------------------------------

""" 
FLOAT
Float, atau "angka titik mengambang" adalah angka, positif atau negatif, yang mengandung satu atau lebih desimal.
"""
h = 1.10
i = 1.0
j = -35.59

print(type(h))
print(type(i))
print(type(j))

# Float juga bisa berupa angka ilmiah dengan "e" untuk menunjukkan kekuatan 10.
# Contoh

k = 35e3
l = 12E4
m = -87.7e100

print(type(k))
print(type(l))
print(type(m))


"""
Kompleks
Bilangan kompleks ditulis dengan "j" sebagai bagian imajiner:
"""
n = 3+5j
o = 5j
p = -5j

print(type(n))
print(type(o))
print(type(p))

# ------------------------------

""" 
Konversi Jenis
Anda dapat mengonversi dari satu jenis ke jenis lainnya dengan metode int(), float(), dan complex():

Contoh
Konversi dari satu jenis ke jenis lainnya:
"""

r = 1   #int
s = 4.1 #float
t = 3j #complex

#convert from int to float:
A = float(r)

#convert from float to int:
B = int(s)

#convert from int to complex:
C = complex(t)

print(A)
print(B)
print(C)

print(type(A))
print(type(B))
print(type(C))

# ------------------------------

""" 
Random number
Python tidak memiliki random()fungsi untuk membuat angka acak, tetapi Python memiliki modul bawaan randomyang disebut yang dapat digunakan untuk membuat angka acak:
"""
import random

print(random.randrange(1, 10))

""" Python Casting
Tentukan Tipe Variabel
Mungkin ada saatnya Anda ingin menentukan tipe pada variabel. Ini bisa dilakukan dengan casting. Python adalah bahasa berorientasi objek, dan karena itu menggunakan kelas untuk mendefinisikan tipe data, termasuk tipe primitifnya.

Casting dengan python dilakukan dengan menggunakan fungsi konstruktor:

int() - membangun bilangan bulat dari literal bilangan bulat, literal float (dengan menghapus semua desimal), atau literal string (menyediakan string mewakili bilangan bulat)
float() - membuat bilangan float dari literal integer, literal float, atau literal string (menyediakan string mewakili float atau integer)
str() - membangun string dari berbagai tipe data, termasuk string, literal integer dan literal float
"""
o = float(1)   # x will be 1.0
p = int(2.8) # y will be 2
q = str(3.0)  # z will be '3.0'