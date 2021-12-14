"Inheritance"
"""
Inheritance/Warisan memungkinkan kita untuk mendefinisikan 
kelas yang mewarisi semua metode dan properti dari kelas lain.

Parent Class adalah kelas yang diwarisi, juga disebut kelas dasar.

Child Class adalah kelas yang mewarisi dari kelas lain, juga disebut kelas turunan.
"""

"""
Buat Parent Class
Kelas apa pun bisa menjadi kelas induk, jadi sintaksnya sama dengan membuat kelas lain:
"""
'Contoh'
'Buat kelas bernama Person, dengan firstnamedan lastnameproperti, dan printnamemetode:'
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

# menggunakan Kelas Person untuk membuat object , 
#  dan lalu mengeksekusi metode printname

x = Person("Nadia", "Fairuzh")
x.printname()
        

""" 
Buat Child Class
Untuk membuat kelas yang mewarisi fungsionalitas dari kelas lain, kirim kelas induk
sebagai parameter saat membuat kelas anak:
"""
'Contoh'
"Buat kelas bernama Student, yang akan mewarisi properti dan metode dari Personkelas:"
class Student(Person):
    pass

"Catatan: Gunakan pass kata kunci saat Anda tidak ingin menambahkan properti atau metode lain ke kelas."

""" Sekarang kelas Siswa memiliki properti dan metode yang sama dengan kelas Person. """

""" 
Gunakan Studentkelas untuk membuat objek, lalu jalankan printnamemetode:
"""
x = Student("Fairis", "Shakira")
x.printname()

"""
Tambahkan Fungsi __init__()
Sejauh ini kita telah membuat kelas anak yang mewarisi properti dan metode dari induknya.

Kami ingin menambahkan __init__()fungsi ke kelas anak (bukan passkata kunci).
"""

'Catatan: The __init__()fungsi disebut secara otomatis setiap kali kelas sedang digunakan untuk membuat objek baru.'

"""
Contoh
Tambahkan __init__()fungsi ke Studentkelas:

class Student(Person):
    def __init__(self, fname, lname):
        #Tambahkan Properti dan lain lain

Saat Anda menambahkan __init__()fungsi, 
kelas anak tidak akan lagi mewarisi fungsi induknya __init__().

Untuk mempertahankan pewarisan fungsi induk __init__() ,
tambahkan panggilan ke fungsi induk __init__():
"""

class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)


"""
Sekarang kita telah berhasil menambahkan fungsi __init__(),
dan mempertahankan warisan dari kelas induk,
dan kita siap untuk menambahkan fungsionalitas dalam __init__()fungsi tersebut
"""

"""
Gunakan Fungsi super()
Python juga memiliki super()fungsi yang akan membuat kelas anak mewarisi 
semua metode dan properti dari induknya:
"""
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)

"""
Dengan menggunakan super()fungsi, Anda tidak harus menggunakan nama elemen induk,
 secara otomatis akan mewarisi metode dan properti dari induknya.
"""

'Tambahkan Properti'
'Tambahkan properti yang dipanggil graduationyearke Studentkelas:'
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2020


"""
Pada contoh di bawah, tahun 2019harus berupa variabel, dan diteruskan ke Studentkelas
 saat membuat objek siswa. Untuk melakukannya, tambahkan parameter lain dalam fungsi __init__():
"""

'Tambahkan year parameter, dan berikan tahun yang benar saat membuat objek:'
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

x = Student("Nadia", "Fairuzh", 2020)
print()

'Tambahkan Metode'
"""
Tambahkan metode yang dipanggil welcomeke Studentkelas:
"""
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):

      
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

# Hasilnya 
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Nadia", "Fairuzh", 2021)
x.welcome()