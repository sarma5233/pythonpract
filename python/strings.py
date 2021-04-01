'''b = " python         practice "
print(b.strip(),"after removing spaces")#remove the uwanted spaces before and after ending
print(b.lstrip())#left
print(b.rstrip())#right



print ("{} is {} new kind of {} experience!".format("python", "totally","learning"))

first_name = "manikanta"
last_name = "sarma"
from_location = "hyderabad"
to_lacation = "pune"
age = "25"

print("{} {} booked bus from {} to {} and his age is {}".format(first_name,last_name,from_location,to_lacation,age))



# %s - String (or any object with a string representation, like numbers)

# %d - Integers

# %f - Floating point numbers

# %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.

# %x/%X - Integers in hex representation (lowercase/uppercase)


print("different type of formatting".title())
name = "srujan"
age = 27
marks_percentage = 78.56
print("%s is %d years old,and he got %f pecentage marks" % (name, age,marks_percentage))




# default arguments
print("Hello {}, your marks pecentage is {}".format("sarma", 78.56).lower())

# positional arguments
print("Hello {0}, your marks pecentage is {1}".format("sarma", 78.56).upper())

# keyword arguments
print("Hello {name}, your marks pecentage is {per}".format(name="sarma", per=78.56).capitalize())

# mixed arguments
print("Hello {0}, your marks pecentage is {per}".format("sarma", per=78.56).swapcase())

print("Joining of strings".upper())

Math_Functions_list1 = ['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc', 'ulp']

Math_Functions = ';--;'.join(Math_Functions_list1)

print(Math_Functions_list1)
print(Math_Functions)

str1 = "hi, my name is, manikanta sarma"

# Without any arguments, the separator is a white-space.
print("Split using default separator:", str1.split()) 
print("Split using ',' as a seperator:", str1.split(',')) 

# Setting maxSplit to 1 means the string is only split once.
print("Split using ',' as a seperator with maxSplit:", str1.split(',',1)) 

print("Split using ',' as a seperator with maxSplit:", str1.split(',', 3)) #3 splits

print("Split using ',' as a seperator with maxSplit:", str1.split(',', 5))  # it is also 3 splits bcz max splits 3


print("Counting substring in the given String:".upper())

string1 = "Betty Botter bought some butter, But she said the butter’s bitter, If I put it in my batter, it will make my batter bitter, But a bit of better butter will make my batter better, So ‘twas better Betty Botter bought a bit of better butter"

print(string1.count("butter"))
print(string1.count("bitter"))

print("finding substrings".title())
string2 = "I saw susie sitting in a shoeshine shop"
print(string2.find("s"))

print(string2.find("s",3,15))

print(string2.find("s",7,15))

print(string2.rfind("s",7,15))'''






print("--"*50)

print("indexing")

string3="She sells seashells by the seashore"

print(string3.index("sells"))


print(string3.index("seashells"))


s="Python programming language"
print(s.index("Python")) # o/p = 0
