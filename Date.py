"Date"

"""
Tanggal Python
Tanggal dalam Python bukanlah tipe datanya sendiri,
 tetapi kita dapat mengimpor modul bernama datetimeuntuk bekerja dengan tanggal sebagai objek tanggal.
"""
'Impor modul datetime dan tampilkan tanggal saat ini:'

import datetime

x = datetime.datetime.now()
print(x)

"""
Keluaran Tanggal
Ketika kita mengeksekusi kode dari contoh di atas, hasilnya adalah:

2021-12-14 13:23:03.403747
Tanggal berisi tahun, bulan, hari, jam, menit, detik, dan mikrodetik.

The datetimemodul memiliki banyak metode untuk kembali informasi tentang obyek date.

Berikut adalah beberapa contoh, Anda akan mempelajarinya lebih lanjut nanti di bab ini:

"""

"Kembalikan tahun dan nama hari kerja:"

import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))

"""
Membuat Objek Tanggal
Untuk membuat tanggal, kita dapat menggunakan datetime()kelas (konstruktor) dari datetimemodul.

The datetime()kelas membutuhkan tiga parameter untuk membuat tanggal: tahun, bulan, hari.
"""
"Buat objek tanggal:"

import datetime

x = datetime.datetime(2020, 5, 17)

print(x)

"""
The datetime()kelas juga mengambil parameter untuk waktu dan zona waktu 
(jam, menit, detik, mikrodetik, tzone), tetapi mereka adalah opsional,
 dan memiliki nilai default 0, ( Nonezona waktu).
"""

"""
Metode strftime()
The datetimeobjek memiliki metode untuk memformat objek tanggal ke string dibaca.

Metode ini dipanggil strftime(), dan mengambil satu parameter, format,
 untuk menentukan format string yang dikembalikan:
"""

"Menampilkan nama bulan:"

import datetime

x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B"))


""""
Referensi semua kode format hukum:

 Directive   	Description	                                                            Example	
    %a	         Weekday, short version                                               	Wed	
    %A	         Weekday, full version	                                                Wednesday	
    %w	         Weekday as a number 0-6, 0 is Sunday	                                   3	
    %d	         Day of month 01-31	                                                       31	
    %b	         Month name, short version                                     	          Dec	
    %B	         Month name, full version                                               December	
    %m	         Month as a number 01-12	                                               12	
    %y	         Year, short version, without century	                                   18	
    %Y	         Year, full version	                                                      2018	
    %H	         Hour 00-23                                                                17	
    %I	         Hour 00-12                                                                05	
    %p	         AM/PM	                                                                   PM  
    %M	         Minute 00-59	                                                           41	
    %S	         Second 00-59	                                                           08	
    %f	         Microsecond 000000-999999	                                              548513	
    %z	         UTC offset	                                                              +0100	
    %Z	         Timezone	                                                               CST	
    %j	         Day number of year 001-366	                                               365	
    %U	         Week number of year, Sunday as the first day of week, 00-53	            52	
    %W	         Week number of year, Monday as the first day of week, 00-53	            52	
    %c	         Local version of date and time	                                  Mon Dec 31 17:41:00 2018	
    %C	         Century	                                                                20	
    %x	         Local version of date                                                 	 12/31/18	
    %X	         Local version of time                                                 	 17:41:00	
    %%	         A % character                                                            	%	
    %G	         ISO 8601 year                                                            	2018	
    %u	         ISO 8601 weekday (1-7)	                                                      1	
    %V	         ISO 8601 weeknumber (01-53)                                               	 01


"""