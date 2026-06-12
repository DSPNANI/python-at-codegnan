Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Bitwise operators
a , b =14 , 7
print(a/b)
2.0
print(a|b)
15
>>> print(a<<b)
1792
>>> print(a>b)
True
>>> print(a>>b)
0
>>> print(a^b)
9
>>> #Membership operator
>>> fruits = ["apple", "banana", "mango"]
>>> print("apple in fruits")
apple in fruits
>>> print("apple" in fruits)
True
>>> print("grapes" in fruits)
False
>>> print("mango" in fruits)
True
>>> #Idenity operators
>>> list1=(1,2,3)
>>> list2=(1,2,3)
>>> print(list1=list2)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    print(list1=list2)
TypeError: print() got an unexpected keyword argument 'list1'
>>> print(list1 is list2)
False
>>> print(list1==list2)
True
