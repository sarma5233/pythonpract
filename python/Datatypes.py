print("DATATYPES")

Student_name = 'Jyothika'
Student_no = 5233
Student_marks_percentage= 75.40

print("Student_name is: ", Student_name)
print("Student_no is: ", Student_no)
print("Student_marks_percentage is: ", Student_marks_percentage)

print()
print("TEXT Type")
print("Student_name type is: ", type(Student_name))#String

print()
print("Numeric Types")
print("Student_no type is: ", type(Student_no))#integer
print("Student_marks_percentage is: ", type(Student_marks_percentage))#Float

print("complex numbers")
print()
a = 10+8j
b = 18-12.8j
c = 24+8.5j

print(a+b)
print(b-c)
print(c+a)
#print(a>b),TypeError: '>' not supported between instances of 'complex' and 'complex'

print()
print("Sequence Types")
print ("LIST")
x = ["ravi", "booni", "kittu","srinu","madhu"]#square brackets are used for list
print(x)
print(type(x))

print("TUPLE")
y = ("sambi","suri","jilani","seshu","george")#Parentheses brackets are used for tuple
print(y)
print(type(y))

print("Range")
u = range(28)
print(u)
print(type(u))

print()
print("SET Types")

print("SET")
z = {"sarma","srujan","vinod","gayathri","manaswi"}#curly brackets are used for tuple
print(z)
print(type(z))

print("Frozenset")
v = frozenset({"sarma","srujan","vinod","gayathri","manaswi"})#curly brackets in Parentheses brackets are used for frozenset
print(v)
print(type(v))


print()
print("Mapping Type")

# empty dictionary
my_dict = {}
print(my_dict)
print(type(my_dict))

# dictionary with integer keys
my_dict1 = {1: 'apple', 2: 'ball'}
print(my_dict1)
print(type(my_dict1))

# dictionary with mixed keys
my_dict2 = {'name': 'John', 1: [2, 4, 3]}
print(my_dict2)
print(type(my_dict2))

# using dict()
my_dict3 = dict({1:'apple', 2:'ball'})
print(my_dict3)
print(type(my_dict3))

# from sequence having each item as a pair
my_dict4 = dict([(1,'apple'), (2,'ball')])
print(my_dict4)
print(type(my_dict4))

print("Boolean Type")
print()
t1 = 10
t2 = 20
num1 = (t1 > t2)
num2 = (t1 == t2)
num3 = (t1 < t2)
num4 = ""
print(num1)
print(num2)
print(num3)
print(bool(num4))
print(type(num1))
print(type(num2))
print(type(num3))
print(type(bool("")))


print()
print("Binary Types")


list1 = [1, 2, 3, 4, 5] 
  

print (type(list1))
list2 = bytes(list1)
print(type(list2))

list3 = bytearray(list1)
print(list1)
print(list2)
print(type(list2))

list4 = memoryview(bytes(list1))
print(list4)
print(type(list4))