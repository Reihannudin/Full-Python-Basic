""" Operator Python
Operator digunakan untuk melakukan operasi pada variabel dan nilai.

Dalam contoh di bawah ini, kami menggunakan +operator untuk menjumlahkan dua nilai:
"""
print(10 + 5)
""" 
Python membagi operator dalam grup berikut:

Operator aritmatika
Operator penugasan
Operator perbandingan
Operator logika
Operator identitas
Operator keanggotaan
Operator bitwise
"""

# --------------------------------------
"""
Operator Aritmatika Python
Operator aritmatika digunakan dengan nilai numerik untuk melakukan operasi matematika umum:
"""
"""
Operator	Name	        Example	
+	        Addition         x + y	
-	        Subtraction      x - y	
*	        Multiplication	 x * y	
/	        Division	     x / y	
%	        Modulus	         x % y	
**	        Exponentiation	 x ** y	
//	        Floor division	 x // y
"""

"""
Operator Penugasan Python
Operator penugasan digunakan untuk menetapkan nilai ke variabel:

Operator   Example	 Same As	
=	       x = 5	 x = 5	
+=	       x += 3	 x = x + 3	
-=	       x -= 3	 x = x - 3	
*=	       x *= 3	 x = x * 3	
/=	       x /= 3	 x = x / 3	
%=	       x %= 3	 x = x % 3	
//=	       x //= 3	 x = x // 3	
**=	       x **= 3	 x = x ** 3	
&=	       x &= 3	 x = x & 3	
|=	       x |= 3	 x = x | 3	
^=	       x ^= 3	 x = x ^ 3	
>>=	       x >>= 3	 x = x >> 3	
<<=	       x <<= 3	 x = x << 3
"""

""" 
Operator Logika Python
Operator logika digunakan untuk menggabungkan pernyataan kondisional:

Operator	Description	                                                 Example	
and 	Returns True if both statements are true	                 x < 5 and  x < 10	
or	    Returns True if one of the statements is true	             x < 5 or x < 4	
not	    Reverse the result, returns False if the result is true	not (x < 5 and x < 10)
"""

""" 
Operator Identitas Python
Operator identitas digunakan untuk membandingkan objek, bukan jika mereka sama, tetapi jika mereka sebenarnya adalah objek yang sama, dengan lokasi memori yang sama:

Operator	Description                                     	        Example	
is      	Returns True if both variables are the same object	        x is y	
is not  	Returns True if both variables are not the same object  	x is not y
"""

""" 
Operator Bitwise Python
Operator bitwise digunakan untuk membandingkan angka (biner):

Operator	Name	                Description
& 	        AND	                    Sets each bit to 1 if both bits are 1
|	        OR	                    Sets each bit to 1 if one of two bits is 1
 ^	        XOR	                    Sets each bit to 1 if only one of two bits is 1
~ 	        NOT	                    Inverts all the bits
<<	        Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off
>>	        Signed right shift	    Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off
"""