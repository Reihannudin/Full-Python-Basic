'Python Scope'

"""
Local Scope
Variabel yang dibuat di dalam fungsi termasuk dalam lingkup lokal fungsi itu,
 dan hanya dapat digunakan di dalam fungsi itu.
"""
'Variabel yang dibuat di dalam fungsi tersedia di dalam fungsi itu:'

def myfunc():
  x = 300
  print(x)

myfunc()

"""
Fungsi Di Dalam Fungsi
Seperti yang dijelaskan dalam contoh di atas,
variabel x tidak tersedia di luar fungsi, 
tetapi tersedia untuk fungsi apa pun di dalam fungsi:
"""
'Variabel lokal dapat diakses dari fungsi di dalam fungsi:'
def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()


""""
Lingkup Global
Variabel yang dibuat di bagian utama kode Python adalah variabel global
 dan termasuk dalam lingkup global.

Variabel global tersedia dari dalam lingkup apapun, global dan lokal
"""
'Variabel yang dibuat di luar fungsi bersifat global dan dapat digunakan oleh siapa saja:'

x = 300

def myfunc():
  print(x)
myfunc()

print(x)


"""
Penamaan Variabel
Jika Anda beroperasi dengan nama variabel yang sama di dalam dan di luar suatu fungsi,
Python akan memperlakukannya sebagai dua variabel terpisah, satu tersedia di lingkup global
(di luar fungsi) dan satu tersedia di lingkup lokal (di dalam fungsi):
"""
'Fungsi akan mencetak local x, dan kemudian kode akan mencetak global x:'

x = 300

def myfunc():
  x = 200
  print(x)
myfunc()

print(x)

"""
Kata Kunci Global
Jika Anda perlu membuat variabel global, tetapi terjebak dalam lingkup lokal,
 Anda dapat menggunakan globalkata kunci.

Kata globalkunci membuat variabel menjadi global.
"""
'Jika Anda menggunakan globalkata kunci, variabel tersebut termasuk dalam lingkup global:'
def myfunc():
  global x
  x = 300
myfunc()

print(x)

'Juga, gunakan global kata kunci jika Anda ingin membuat perubahan pada variabel global di dalam suatu fungsi.'


'Untuk mengubah nilai variabel global di dalam suatu fungsi, lihat variabel tersebut dengan menggunakan globalkata kunci:'
x = 300
def myfunc():
  global x
  x = 200
myfunc()

print(x)

