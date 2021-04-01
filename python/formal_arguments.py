
def my_function():
  print("Hello from a function")

my_function() # calling function(if we write calling funtion two times, it'll give the same o/p two times)


def my_friends(fname):
  print(fname + " BFF")

my_friends("Naveen")
my_friends("jyothika")
my_friends("Srujan")


print("<->"*50)


def my_fruits(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry","dragon","kiwi"]

my_fruits(fruits)

print("<->"*50)


def sum(num1,num2): #formal arguments and function definition 
    print("it'll print")
    return num1 * num2
    print("it'll not print")


print(sum(5,2)) # actual arguments and caller funtion
print(sum(10000,0.9876))
print(sum(15420,57745))

'''def cart(item=1, price): #non-default argument follows default argument
   print(item, "cost is :" ,price)

cart(item="pen")
cart(item="handbag", price=10000)
cart(price=500, item="shirt")'''

print("<->"*50)

def cart(price,item="tv"):
 print(item, "cost is :" ,price)

cart(price="pen")
cart(item="handbag", price=10000)
cart(price=500, item="shirt")

print("<->"*50)

def checking(num):
   if num % 2 == 0:
       print(num," is even")
   else:
       print(num," is odd")
checking(12)
checking(31)