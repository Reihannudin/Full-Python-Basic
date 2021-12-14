""""
The tryblok memungkinkan Anda menguji blok kode kesalahan.

The exceptblok memungkinkan Anda menangani kesalahan.

The finallyblok memungkinkan Anda mengeksekusi kode,
 terlepas dari hasil coba-dan kecuali blok.
"""
"""
Penanganan Pengecualian
Ketika terjadi kesalahan, atau pengecualian seperti yang kita sebut,
 Python biasanya akan berhenti dan menghasilkan pesan kesalahan.

Pengecualian ini dapat ditangani menggunakan trypernyataan:
"""
'The tryblock akan menghasilkan pengecualian, karena xtidak didefinisikan:'

'''
try:
  print(x)
except:
  print("An exception occurred")
  '''

'''
Karena blok try menimbulkan kesalahan, blok exception akan dieksekusi.

Tanpa blok coba, program akan macet dan menimbulkan kesalahan:
'''

'''
Banyak Pengecualian
Anda dapat menentukan blok pengecualian sebanyak yang Anda inginkan,
 misalnya jika Anda ingin mengeksekusi blok kode khusus untuk jenis kesalahan khusus:
'''
'Cetak satu pesan jika blok coba memunculkan a NameErrordan yang lain untuk kesalahan lain:'
'''
try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")
'''
'''
  Else
  Anda dapat menggunakan elsekata kunci untuk menentukan blok kode yang akan dieksekusi
   jika tidak ada kesalahan yang muncul:
  '''
' Dalam contoh ini, tryblok tidak menghasilkan kesalahan apa pun:'

try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")

"""
Finally
The finallyblok, bila ditentukan, akan dieksekusi terlepas jika blok try menimbulkan kesalahan atau tidak.
"""
'''
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")
'''
'Ini dapat berguna untuk menutup objek dan membersihkan sumber daya'
"""
coba buka dan tulis ke file yang tidak dapat ditulis:
"""
try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")

'Program dapat dilanjutkan, tanpa membiarkan objek file terbuka'

'''
Naikkan pengecualian
Sebagai pengembang Python, Anda dapat memilih untuk melempar pengecualian jika suatu kondisi terjadi.

Untuk melempar (atau menaikkan) pengecualian, gunakan raisekata kunci.
'''
'Naikkan kesalahan dan hentikan program jika x lebih rendah dari 0:'

x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")

'''
Kata raisekunci digunakan untuk memunculkan pengecualian.

Anda dapat menentukan jenis kesalahan apa yang akan muncul,
 dan teks yang akan dicetak kepada pengguna.
'''
'Naikkan TypeError jika x bukan bilangan bulat:'

x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")