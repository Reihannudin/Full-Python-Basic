'Array'

"""
Apa itu Array?
Array adalah variabel khusus, yang dapat menampung lebih dari satu nilai pada satu waktu.

Jika Anda memiliki daftar item (daftar nama mobil, misalnya), menyimpan mobil dalam variabel
tunggal dapat terlihat seperti ini:
"""
car1 = "Ford"
car2 = "Volvo"
car3 = "BMW"
cars = ["Ford", "Volvo", "BMW"]
"""
Namun, bagaimana jika Anda ingin menelusuri mobil dan menemukan yang spesifik? Dan bagaimana 
jika Anda tidak memiliki 3 mobil, tetapi 300?

Solusinya adalah array!

Array dapat menampung banyak nilai di bawah satu nama, dan Anda dapat mengakses nilai dengan
 merujuk ke nomor indeks.
"""

# ---------------------------------------------

'''
Akses Elemen Array
Anda merujuk ke elemen array dengan mengacu pada nomor indeks .
'''

'Dapatkan nilai item array pertama:'
x = cars[0]

'Ubah nilai item array pertama:'
cars[0] = "Toyota"
print(cars)

"""
Panjang Array
Gunakan len()metode untuk mengembalikan panjang array 
(jumlah elemen dalam array).
"""
x = len(cars)

"""
Elemen Array Pengulangan
Anda dapat menggunakan for inloop untuk mengulang semua elemen array.
"""
for x in cars:
  print(x)

"""
Menambahkan Elemen Array
Anda dapat menggunakan append()metode untuk menambahkan elemen ke array.
"""
cars.append("Honda")
print(cars)

"""
Menghapus Elemen Array
Anda dapat menggunakan pop()metode untuk menghapus elemen dari array.
"""
cars.pop(1)
print(cars)

"""
Anda juga dapat menggunakan remove()metode untuk menghapus elemen dari array.
"""
cars.remove("BMW")
print(cars)
'Catatan: Metode daftar remove()hanya menghapus kemunculan pertama dari nilai yang ditentukan.'


"""
Metode Array
Python memiliki seperangkat metode bawaan yang dapat Anda gunakan pada daftar/array.

Method	    Description
append()	Adds an element at the end of the list
clear()	    Removes all the elements from the list
copy()	    Returns a copy of the list
count()	    Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	    Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	    Removes the element at the specified position
remove()	Removes the first item with the specified value
reverse()	Reverses the order of the list
sort()	    Sorts the list
Catatan:    Python tidak memiliki dukungan bawaan untuk Array, tetapi Daftar Python dapat digunakan sebagai gantinya.
"""