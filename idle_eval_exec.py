Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> eval()
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    eval()
TypeError: eval expected at least 1 argument, got 0
>>> 
>>> eval('a = 5')
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    eval('a = 5')
  File "<string>", line 1
    a = 5
      ^
SyntaxError: invalid syntax
>>> exec('a = 5')
>>> a
5
>>> def calc(x,y):
	return x + y

>>> eval('calc(4,5)')
9
>>> exec('calc(4,5)')
>>> def calc(x,y):
	print(x + y)

	
>>> eval('calc(4,5)')
9
>>> exec('calc(4,5)')
9
>>> def calc(x,y):
	print("Sum is",x + y)

	
>>> eval('calc(4,5)')
Sum is 9
>>> exec('calc(4,5)')
Sum is 9
>>> eval('12+3/4/12+12-12-3-5+12')
16.0625
>>> exec('12+3/4/12+12-12-3-5+12')
>>> exec('for i in range(5):print(i)')
0
1
2
3
4
>>> eval('for i in range(5):print(i)')
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    eval('for i in range(5):print(i)')
  File "<string>", line 1
    for i in range(5):print(i)
    ^
SyntaxError: invalid syntax
>>> 