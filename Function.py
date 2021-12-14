'Function'
"""
Fungsi adalah blok kode yang hanya berjalan ketika dipanggil.

Anda dapat meneruskan data, yang dikenal sebagai parameter, ke dalam suatu fungsi.

Sebuah fungsi dapat mengembalikan data sebagai hasilnya.
"""

"""
Membuat Fungsi
Dalam Python, sebuah fungsi didefinisikan menggunakan kata kunci def :
"""
def my_function():
    print("Hello I'm Function")

'Memanggil Fungsi'
'Untuk memanggil fungsi, gunakan nama fungsi diikuti dengan tanda kurung:'

my_function()

# ------------------------------------

'Argument'
"""
Informasi dapat diteruskan ke fungsi sebagai argumen.

Argumen ditentukan setelah nama fungsi, di dalam tanda kurung. 
Anda dapat menambahkan argumen sebanyak yang Anda inginkan, cukup pisahkan dengan koma.

Contoh berikut memiliki fungsi dengan satu argumen (fname).
Saat fungsi dipanggil, kami memberikan nama depan, yang digunakan 
di dalam fungsi untuk mencetak nama lengkap:
"""
def my_function(fname):
    print(fname + " Refsnes")

my_function("Nadia")
my_function("Fairis")
my_function("Han")

'Argumen sering disingkat menjadi args dalam dokumentasi Python.'

'Parameters or Arguments?'
"""
Istilah parameter dan argumen dapat digunakan untuk hal yang sama:
 informasi yang diteruskan ke suatu fungsi.
"""
"""
Dari perspektif fungsi:

Parameter adalah variabel yang terdaftar di dalam tanda kurung dalam definisi fungsi.

Argumen adalah nilai yang dikirim ke fungsi saat dipanggil
"""

"""
Jumlah Argumen
Secara default, suatu fungsi harus dipanggil dengan jumlah argumen yang benar.
 Artinya jika fungsi Anda mengharapkan 2 argumen, Anda harus memanggil fungsi dengan 2 argumen,
 tidak lebih, dan tidak kurang.
"""
'Contoh Fungsi yang mengharapkan 2 argumen, dan mendapat 2 argumen:'

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Nadia", "Fairuzh")

'Jika Anda mencoba memanggil fungsi dengan 1 atau 3 argumen, Anda akan mendapatkan kesalahan:'

"""
Error Function
# def my_function(fname, lname):
# print(fname + " " + lname)

# my_function("Emil"
"""

"""
Argumen Sewenang-wenang, *args
Jika Anda tidak tahu berapa banyak argumen yang akan diteruskan ke fungsi Anda,
tambahkan a *sebelum nama parameter dalam definisi fungsi.

Dengan cara ini fungsi akan menerima tupel argumen, dan dapat mengakses item yang sesuai:
"""
'Jika jumlah argumen tidak diketahui, tambahkan a *sebelum nama parameter:'
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")
'Argumen Sewenang-wenang sering disingkat menjadi *args dalam dokumentasi Python.'

"""
KeyWord Argumen 
Anda juga dapat mengirim argumen dengan sintaks kunci = nilai .

Dengan cara ini urutan argumen tidak menjadi masalah.
"""
def my_function(child3, child2, child1):
    print("The Youngest child is " + child3)

my_function(child1= "Fairis", child2="Han", child3="Nadia")

'Frase Argumen Kata Kunci sering disingkat menjadi kwargs dalam dokumentasi Python.'

"""
Arbitrary Keyword Arguments, **kwargs

Jika Anda tidak tahu berapa banyak argumen kata kunci yang akan diteruskan ke fungsi Anda, 
tambahkan dua tanda bintang: **sebelum nama parameter dalam definisi fungsi.

Dengan cara ini fungsi akan menerima kamus argumen, dan dapat mengakses item yang sesuai:
"""
'Jika jumlah argumen kata kunci tidak diketahui, tambahkan ganda **sebelum nama parameter:'

def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")
'Argumen Kword Sewenang-wenang sering disingkat menjadi **kwargs dalam dokumentasi Python.'


'Default Parameter Value'
"""
Contoh berikut menunjukkan cara menggunakan nilai parameter default.

Jika kita memanggil fungsi tanpa argumen, ia menggunakan nilai default:
"""
def my_function(country = "Indonesia"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

"""
Melewati Daftar sebagai Argumen
Anda dapat mengirim argumen tipe data apa pun ke suatu fungsi 
(string, angka, daftar, kamus, dll.), dan itu akan diperlakukan
 sebagai tipe data yang sama di dalam fungsi.

Misalnya jika Anda mengirim Daftar sebagai argumen, itu akan tetap menjadi
 Daftar ketika mencapai fungsi:
"""
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)


'Mengembalikan Nilai'
'''Untuk membiarkan suatu fungsi mengembalikan nilai, gunakan return pernyataan:'''
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

'Pass Statement'
""" 
Pernyataan lulus
functiondefinisi tidak boleh kosong, tetapi jika Anda karena alasan tertentu 
memiliki functiondefinisi tanpa konten, masukkan passpernyataan untuk menghindari kesalahan.
"""
def myfunction():
    pass

"""
Pengulangan
Python juga menerima rekursi fungsi, yang berarti fungsi yang ditentukan dapat memanggil dirinya sendiri.

Rekursi adalah konsep matematika dan pemrograman yang umum. Ini berarti bahwa suatu fungsi memanggil
dirinya sendiri. Ini memiliki manfaat yang berarti bahwa Anda dapat mengulang data untuk mencapai hasil.

Pengembang harus sangat berhati-hati dengan rekursi karena dapat dengan mudah tergelincir ke dalam penulisan
fungsi yang tidak pernah berhenti, atau fungsi yang menggunakan jumlah memori atau daya prosesor yang berlebihan.
Namun, ketika ditulis dengan benar, rekursi bisa menjadi pendekatan pemrograman yang sangat efisien dan elegan
secara matematis.

Dalam contoh ini, tri_recursion() adalah fungsi yang telah kita definisikan untuk memanggil dirinya sendiri ("recurse").
Kami menggunakan variabel k sebagai data, yang mengurangi ( -1 ) setiap kali kami melakukan pengulangan.
Rekursi berakhir ketika kondisinya tidak lebih besar dari 0 (yaitu ketika 0).

Bagi pengembang baru, perlu beberapa waktu untuk mengetahui cara kerjanya, cara terbaik untuk mengetahuinya 
adalah dengan menguji dan memodifikasinya.
"""
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)