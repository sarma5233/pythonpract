print("Default")

def frnds(name, age = "30"):
   #This function displays the name and age of a person

   #If age is not provided,it's default value 30 would be displayed.

   print(name + " is " + age + " years old")

frnds("naveen")
frnds("jyothika", "25")
frnds("srujan", "27")

print("<->"*50)
print("Keyword")

def emp_list(name, age):
   print(name + " is " + age + " years old")

# 2 keyword arguments (In order)
emp_list(name = "naveen", age = "30")

# 2 keyword arguments (Not in order)
emp_list(age = "25", name = "jyohika")

# 1 positional and 1 keyword argument
emp_list("srujan", age = "27")


print("<->"*50)
print("Arbitrary")

def greet(*employees):
#This function greets all the person in the names tuple.

    # names is a tuple with arguments
    for name in employees:
        print("Hello", name)
greet("naveen", "srujan", "jyothika", "krishna")

print("<->"*50)
print("returning multiple values")

def getPerson():
    name = "seshu"
    age = 30
    country = "india"
    return name,age,country

name,age,country = getPerson()
print(name)
print(age)
print(country)


print("<->"*50)