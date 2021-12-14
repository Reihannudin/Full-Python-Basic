"""String Python
string
String dalam python dikelilingi oleh tanda kutip tunggal, atau tanda kutip ganda.

'halo' sama dengan 'halo' .

Anda dapat menampilkan string literal dengan print()fungsi:
"""
print("Hello")
print('Hello')

# ------------------------------

""" 
Tetapkan String ke Variabel
Menetapkan string ke variabel dilakukan dengan nama variabel diikuti dengan tanda sama dengan dan string:
"""
a = "Hello"
print(a)

# ------------------------------

""" 
String Multiline
Anda dapat menetapkan string multiline ke variabel dengan menggunakan tiga tanda kutip:
"""
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
# Atau tiga kutipan tunggal:
b = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(b)

# ------------------------------

""" 
String adalah Array
Seperti banyak bahasa pemrograman populer lainnya, string dalam Python adalah array byte yang mewakili karakter unicode.

Namun, Python tidak memiliki tipe data karakter, satu karakter hanyalah string dengan panjang 1.

Tanda kurung siku dapat digunakan untuk mengakses elemen string.
"""
a = "Hello, World!"
print(a[1])

# ------------------------------

""" 
Looping Melalui String
Karena string adalah array, kita dapat mengulang karakter dalam string, dengan forloop.
"""
for x in "banana":
  print(x)

# ------------------------------


""" 
String Length
Untuk mendapatkan panjang string, gunakan len()fungsi.
"""
a = "Hello, World!"
print(len(a))

# ------------------------------

"""
Check String
Untuk memeriksa apakah ada frase atau karakter tertentu dalam sebuah string, kita dapat menggunakan kata kunci in.
"""
txt = "The best things in life are free!"
print("free" in txt)

# Gunakan dalam sebuah ifpernyataan:
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

# ------------------------------

"""
Periksa apakah NOT
Untuk memeriksa apakah frasa atau karakter tertentu TIDAK ada dalam string, kita dapat menggunakan kata kunci not in.
"""
txt = "The best things in life are free!"
print("expensive" not in txt)
# Gunakan dalam sebuah ifpernyataan:
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

# ------------------------------

"""Python - Slicing Strings
Slicing
Anda dapat mengembalikan rentang karakter dengan menggunakan sintaks irisan.

Tentukan indeks awal dan indeks akhir, dipisahkan oleh titik dua, untuk mengembalikan bagian dari string.

Dapatkan karakter dari posisi 2 ke posisi 5 (tidak termasuk):
"""
b = "Hello, World!"
print(b[2:5])

""" 
Iris Dari Awal
Dengan mengabaikan indeks awal, rentang akan dimulai pada karakter pertama:
"""
b = "Hello, World!"
print(b[:5])

""" 
Iris Sampai Akhir
Dengan mengabaikan indeks akhir , rentang akan berakhir:
"""
b = "Hello, World!"
print(b[2:])

""" 
Pengindeksan Negatif
Gunakan indeks negatif untuk memulai irisan dari akhir string:
"""
b = "Hello, World!"
print(b[-5:-2])

# ------------------------------

""" Python - Modify Strings 
"""
""" Upper Case 
The upper()Metode mengembalikan string dalam huruf besar:
"""
a = "Hello, World!"
print(a.upper())

""" Lower Case 
The lower()Metode mengembalikan string dalam huruf kecil:
"""
a = "Hello, World!"
print(a.lower())

""" Remove Whitespace 
Spasi putih adalah spasi sebelum dan/atau setelah teks yang sebenarnya, dan sangat sering Anda ingin menghapus spasi ini."""
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

""" Replace String 
The replace()Metode menggantikan string dengan string lain: """
a = "Hello, World!"
print(a.replace("H", "J"))

""" Split String 
The split()Metode mengembalikan daftar di mana teks antara pemisah yang ditentukan menjadi item daftar.
 """
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

# ------------------------------

""" String Concatenation
Untuk menggabungkan, atau menggabungkan, dua string Anda dapat menggunakan operator +.
"""
a = "Hello"
b = "World"
c = a + b
print(c)

a = "Hello"
b = "World"
c = a + " " + b
print(c)

# ------------------------------
"""
String Format
Seperti yang kita pelajari di bab Variabel Python, kita tidak dapat menggabungkan string dan angka seperti ini:
"""
age = 36
txt = "My name is John, I am " + age
print(txt)

"""Tapi kita bisa menggabungkan string dan angka dengan menggunakan format()metode!

The format()metode mengambil argumen berlalu, format mereka, dan tempat-tempat mereka dalam string mana placeholder {}adalah:
"""
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

# Metode format() mengambil argumen dalam jumlah tak terbatas, dan ditempatkan ke masing-masing placeholder:
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

# Anda dapat menggunakan nomor indeks {0}untuk memastikan argumen ditempatkan di tempat penampung yang benar:
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

""" Escape Character
karakter pelarian
Untuk menyisipkan karakter yang ilegal dalam string, gunakan karakter escape.

Karakter escape adalah garis miring terbalik yang \diikuti oleh karakter yang ingin Anda sisipkan.

Contoh karakter ilegal adalah tanda kutip ganda di dalam string yang dikelilingi oleh tanda kutip ganda:
"""
# txt = "We are the so-called "Vikings" from the north."

"""Untuk memperbaiki masalah ini, gunakan karakter escape \":"""

txt = "We are the so-called \"Vikings\" from the north."
"""
\'	Single Quote	
\\	Backslash	
\n	New Line	
\r	Carriage Return	
\t	Tab	
\b	Backspace	
\f	Form Feed	
\ooo	Octal value	
\xhh	Hex value
"""

""" String Methods
Python memiliki seperangkat metode bawaan yang dapat Anda gunakan pada string.

Catatan: Semua metode string mengembalikan nilai baru. Mereka tidak mengubah string asli."""

""" lihat disini https://www.w3schools.com/python/python_strings_methods.asp"""