"""
VARIABEL 

Python tidak memiliki perintah untuk mendeklarasikan variabel.
Variabel dibuat saat Anda pertama kali menetapkan nilai padanya
"""

# ------------------------------
"""
Membuat Variable 

Python tidak memiliki perintah untuk mendeklarasikan variabel.
Variabel dibuat saat Anda pertama kali menetapkan nilai padanya.
Contoh """

n = "Nutty"
r = "Han"
print(n)
print(r)

# ------------------------------

""" membuat variable casting
Jika Anda ingin menentukan tipe data dari suatu variabel, ini dapat dilakukan dengan casting. """

x= str(3) # ini akan menjadi 3 akan tetapi dalam tipe data string
y= int(3) # ini akan menjadi 3 akan tetapi dalam tipe data Integer
z= float(3) # ini akan menjadi 3 akan tetapi dalam tipe data Float
print(type(x))
print(type(y))

# ------------------------------

"""
Hal - hal sensitif
Nama variabel peka huruf besar/kecil.
"""
a = "Spiderman"
A = 4

# ------------------------------

"""
Nama Variabel
Sebuah variabel dapat memiliki nama pendek (seperti x dan y) atau nama yang lebih deskriptif (umur, carname, total_volume). Aturan untuk variabel Python:
Nama variabel harus dimulai dengan huruf atau karakter garis bawah
Nama variabel tidak boleh diawali dengan angka
Nama variabel hanya boleh berisi karakter alfanumerik dan garis bawah (Az, 0-9, dan _ )
Nama variabel peka huruf besar/kecil (usia, Usia, dan AGE adalah tiga variabel berbeda)
"""

myvar = "Seokjin"
my_var = "Seokjin"
my__var = "Seokjin"
MYvar = "Seokjin"
myVar ="Seokjin"

# ------------------------------

"""
Nama Variabel Multi Kata
Nama variabel dengan lebih dari satu kata bisa jadi sulit dibaca.
Ada beberapa teknik yang dapat Anda gunakan untuk membuatnya lebih mudah dibaca:
"""
"""
Kasus unta
Setiap kata, kecuali yang pertama, dimulai dengan huruf kapital:
"""
myVariableName = "John"
"""
Kasus Pascal
Setiap kata dimulai dengan huruf kapital:
"""
MyVariableName = "John"
"""
Kasus Ular
Setiap kata dipisahkan oleh karakter garis bawah:
"""
my_variable_name = "John"

# ------------------------------

""" 
Banyak Nilai ke Beberapa Variabel
Python memungkinkan Anda untuk menetapkan nilai ke beberapa variabel dalam satu baris:
"""

s ,t ,u = "Sapi", "Tempe" , "Cherry"
print(s)
print(t)
print(u)

# ------------------------------

"""
Satu Nilai ke Beberapa Variabel
Dan Anda dapat menetapkan nilai yang sama ke beberapa variabel dalam satu baris:
"""
f = d = "Iceee"
print(f)
print(d)

# ------------------------------

""" Membongkar Koleksi
Jika Anda memiliki kumpulan nilai dalam daftar, tuple, dll. Python memungkinkan Anda mengekstrak nilai ke dalam variabel. Ini disebut membongkar .
"""
buah = [ "apel", "nanas", "jeruk"]
g, h, j = buah
print(g)
print(h)
print(j)

# ------------------------------

""" Variabel Keluaran
printPernyataan Python sering digunakan untuk mengeluarkan variabel.

Untuk menggabungkan teks dan variabel, Python menggunakan +karakter:
"""

F = "Beautifull"
print("Nutty is " + F)
# Anda juga dapat menggunakan +karakter untuk menambahkan variabel ke variabel lain:

# Untuk angka, +karakter berfungsi sebagai operator matematika:
J = 41
K = 91
print(J + K)

# ------------------------------

""" Variabel Global
Variabel yang dibuat di luar fungsi (seperti dalam semua contoh di atas) dikenal sebagai variabel global.

Variabel global dapat digunakan oleh semua orang, baik di dalam fungsi maupun di luar. 
"""
# Buat variabel di luar fungsi, dan gunakan di dalam fungsi

R = "awesome"

def myfunc():
    print("Python is " + R)

myfunc()

"""
Jika Anda membuat variabel dengan nama yang sama di dalam suatu fungsi, variabel ini akan bersifat lokal, 
dan hanya dapat digunakan di dalam fungsi tersebut. Variabel global dengan nama yang sama akan tetap seperti semula,
global dan dengan nilai aslinya.
"""

B = "Butter"

def Bfunc():
    B = "Cherry"
    print("Smooth like " + B)

Bfunc()

print("Smooth like " + B)

"""
Kata Kunci global
Biasanya, ketika Anda membuat variabel di dalam suatu fungsi, variabel itu bersifat lokal, dan hanya dapat digunakan di dalam fungsi itu.

Untuk membuat variabel global di dalam suatu fungsi, Anda dapat menggunakan globalkata kunci.

CONTOH :
Jika Anda menggunakan global kata kunci, variabel tersebut termasuk dalam lingkup global:
"""
def Bfunc():
    global B
    B = "Ball"

Bfunc()

print("Python is " + B)
