"Python Matematika"
"""
Python memiliki seperangkat fungsi matematika bawaan,
 termasuk modul matematika ekstensif, 
 yang memungkinkan Anda melakukan tugas matematika pada angka.

"""

"""
Fungsi Matematika Bawaan
Fungsi min()and max()dapat digunakan untuk menemukan nilai terendah
 atau tertinggi dalam iterable:
"""
x = min(5, 10, 25)
y = max(5, 10, 25)

print(x)
print(y)

'The abs()mengembalikan fungsi (positif) nilai absolut dari jumlah yang ditentukan:'
x = abs(-7.25)

print(x)

"The fungsi mengembalikan nilai x dengan kekuatan y (x y ).pow(x, y)"
x = pow(4, 3)

print(x)

"""
Modul Matematika
Python juga memiliki modul bawaan yang disebut math, yang memperluas daftar fungsi matematika.

Untuk menggunakannya, Anda harus mengimpor mathmodul:
"""
import math
"""
Setelah Anda mengimpor mathmodul, Anda dapat mulai menggunakan metode dan konstanta modul.

The math.sqrt()Metode misalnya, mengembalikan akar kuadrat dari angka:
"""
import math

x = math.sqrt(64)

print(x)

"""
The math.ceil()Metode putaran sejumlah atas untuk bilangan bulat terdekat, 
dan math.floor() metode putaran sejumlah bawah ke integer terdekat, dan kembali hasilnya:
"""
import math

x = math.ceil(1.4)
y = math.floor(1.4)

print(x) # returns 2
print(y) # returns 

"The math.pikonstan, mengembalikan nilai PI (3.14 ...):"
import math

x = math.pi

print(x)