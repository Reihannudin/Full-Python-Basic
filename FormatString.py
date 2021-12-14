'Pemformatan String Python'

'''
format string()
The format()Metode memungkinkan Anda untuk format yang dipilih bagian dari string.

Terkadang ada bagian teks yang tidak Anda kendalikan, mungkin berasal dari database, atau input pengguna?

Untuk mengontrol nilai tersebut, tambahkan placeholder (tanda kurung kurawal {}) dalam teks, 
dan jalankan nilai melalui format()metode:
'''
'Tambahkan placeholder tempat Anda ingin menampilkan harga:'

price = 49
txt = "The price is {} dollars"
print(txt.format(price))

'Anda dapat menambahkan parameter di dalam tanda kurung kurawal untuk menentukan cara mengonversi nilai:'
'Format harga yang akan ditampilkan sebagai angka dengan dua desimal:'
txt = "The price is {:.2f} dollars"

"""
Beberapa Nilai
Jika Anda ingin menggunakan lebih banyak nilai, tambahkan saja lebih banyak nilai ke metode format():
"""
print(txt.format(price,' itemno, count'))

'Dan tambahkan lebih banyak placeholder:'

quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))

'''
Nomor Indeks
Anda dapat menggunakan nomor indeks (angka di dalam tanda kurung kurawal {0})
 untuk memastikan nilai ditempatkan di tempat penampung yang benar:
'''
quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))

'Juga, jika Anda ingin merujuk ke nilai yang sama lebih dari sekali, gunakan nomor indeks:'

age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))

'''
Indeks Bernama
Anda juga dapat menggunakan indeks bernama dengan memasukkan nama di dalam tanda kurung kurawal
 {carname}, tetapi kemudian Anda harus menggunakan nama saat Anda meneruskan nilai parameter 
 txt.format(carname = "Ford"):
'''
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))