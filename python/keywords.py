import keyword
print(keyword.kwlist)
print("KEYWORD LIST")
#['False', 'None', 'True', '__peg_parser__', 'and', 'as', 'assert', 'async', 'await', 'break', 
#'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global',
#'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 
# while', 'with', 'yield']
print()
print("TRUE,FALSE")
print (False == 0) 
print (True == 1) 
  
print (False + False + True) 
print (True + False + False)

print("NONE")
a = None
print(a)
print(type(a))
#2nd example
print(print("Hello, World!"))


print("AND,OR,NOT")

x = True
y = False

print(x and y)
print(x or y)
print(not(x))

print("AS, FROM")
import math as ss
print(dir(ss))
print(ss.factorial(10))
print(ss.ceil(100.5))
print(ss.floor(45.68))
#print(help('modules'))

import math
from math import factorial
print(math.factorial(10))

from datetime import date


class Date():
    def __init__(self,date,month,year):
        self.date = date
        self.month = month
        self.year = year

    def wish(self):
        print(self.date,self.month,self.year)

date1 = date(12,01,2021)
