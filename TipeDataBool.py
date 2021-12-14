""" Nilai Boolean
Dalam pemrograman, Anda sering perlu mengetahui apakah suatu ekspresi adalah Trueatau False.

Anda dapat mengevaluasi ekspresi apa pun dengan Python, dan mendapatkan salah satu dari dua jawaban, Trueatau False.

Saat Anda membandingkan dua nilai, ekspresi dievaluasi dan Python mengembalikan jawaban Boolean:
"""
print(10 > 9)
print(10 == 9)
print(10 < 9)

"""Saat Anda menjalankan kondisi dalam pernyataan if, Python mengembalikan Trueatau False:"""
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")


"""Evaluasi Nilai dan Variabel
The bool()fungsi memungkinkan Anda untuk mengevaluasi nilai apapun, dan memberikan Trueatau False imbalan,
"""
print(bool("Hello"))
print(bool(15))

""" Fungsi dapat Mengembalikan Boolean
Anda dapat membuat fungsi yang mengembalikan Nilai Boolean:"""
def myFunction() :
  return True

print(myFunction())

""" Python juga memiliki banyak fungsi bawaan yang mengembalikan nilai boolean, seperti isinstance() fungsi, 
yang dapat digunakan untuk menentukan apakah suatu objek memiliki tipe data tertentu:"""
x = 200
print(isinstance(x, int))