'While Loop'
"""
Dengan perulangan while kita dapat mengeksekusi satu set pernyataan selama
kondisinya benar.
"""
'Cetak i selama i kurang dari 6:'

i = 1
while i <= 6:
  print(i)
  i += 1

'''
Catatan: ingat untuk menambah i, atau loop akan berlanjut selamanya.

The sedangkan lingkaran membutuhkan variabel yang relevan untuk siap, 
dalam contoh ini kita perlu mendefinisikan variabel pengindeksan, i ,
yang kita set ke 1.
'''

'The break Statement'
"""
Dengan pernyataan break kita dapat menghentikan perulangan meskipun kondisi while benar:
"""
j = 1
while j < 6:
  print(j)
  if j == 3:
    break
  j += 1

'The continue Statement'
"""
Dengan pernyataan continue kita dapat menghentikan iterasi saat ini, dan melanjutkan dengan yang berikutnya:
"""
'Lanjutkan ke iterasi berikutnya jika i adalah 3:'
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

'The else Statement'
"""
  Dengan pernyataan else kita dapat menjalankan blok kode satu kali ketika kondisinya tidak lagi benar:
"""
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")