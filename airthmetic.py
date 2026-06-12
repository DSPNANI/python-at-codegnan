Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=20 , b=30
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
>>> a , b = 20 ,30
>>> print(a+b)
50
>>> print(a-b)
-10
>>> print(b-a)
10
>>> print(a*b)
600
>>> print(a/b)
0.6666666666666666
>>> print(a%b)
20
>>> print(a//b)
0
print(a+=2)
