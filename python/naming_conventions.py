class Students():
    def __init__(self,name,rollno,marks):
        self.name =name
        self.rollno = rollno
        self.marks = marks

    def wish(self):
        print(self.name,self.rollno,self.marks)

_Student1 = Students("ravi",5233,48)
Student2 = Students("shankar",8899,33)
print(_Student1)
print(Student2)

_Student1.wish()#starts with _ indicates private variable
Student2.wish()#public variable
import math
print(dir(math))
print(math.factorial(10))
print(math.ceil(100.5))
print(math.floor(45.68))
print(help(math.exp))#it will give you the syntax and explanation about the datatype

import Datatypes
print(dir())

#import operators
#print(dir())