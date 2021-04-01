# Python Program for 
# Creation of String 
  
# Creating a String  
# with single Quotes 
String1 = 'Welcome to the beautiful World'
print("String with the use of Single Quotes: ") 
print(String1) 
  
# Creating a String 
# with double Quotes 
String2 = "My Name is Sarma"
print("\nString with the use of Double Quotes: ") 
print(String2) 
  
# Creating a String 
# with triple Quotes 
String3 = '''My Name is Sarma and I live in a world of "Peace"'''
print("\nString with the use of Triple Quotes: ") 
print(String3) 
  
# Creating String with triple 
# Quotes allows multiple lines 
# Assign String to a Variable
a = '''Nature 
            is 
            Beautiful'''
print("\nCreating a multiline String: ") 
print(a) 


# Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.
# However, Python does not have a character data type, a single character is simply a string with a length of 1.
# Square brackets can be used to access elements of the string.


#modification of strings

string4 = "i'm very lucky"
print(string4.upper())
print(string4[5])#Positive Direction starts from 0
print(string4[-9])#Negative (Reverse) Direction starts from -1



print("slicing and indexing and modification".upper())

a = "Python Practice"
#--> 0123456789....14
#   -15......-4-3-2-1 <--
print("TOTAL")
print(a[::])#it'll take starting value as 0 and stop value is ending value
print("Negative Direction".lower())
print(a[-1:-7:-2]) # [start:stop:step value]

print("Positive Direction".upper())
print(a[1:12:3])

b = " python "
print(b.strip(),"after removing spaces")#remove the uwanted spaces before and after ending
print(b.lstrip())#left
print(b.rstrip())#right
print(b.replace("t","h"))#replacing characters using letters

list1 = ['sarma','charan','siva','manikanta',89,52,65] #lists we can change using index number

print(list1[4])
list1[4]="gowrav"
print(list1)


print("String concatenation".upper())

m = "python"
n = "practice"
o = m + n
p = m + " " + n
print(o)
print(p)


s = "python practice "
r = 12
g = s * r
print(g)
print(len(s))
print(len(g))

print("pract" in s)
print("Python" in s)#it'll give you the result as false, bcz python language is case sensitive
print ("12" not in s)
print("pyThon" not in s)#it'll give you the result as true, bcz python language is case sensitive


x = 4
y = 8
list = [1, 2, 3, 4, 5]
if ( x in list ):
   print("x is available in the given list")
else:
   print("x is not available in the given list")
if ( y not in list ):
   print("y is not available in the given list")
else:
   print("y is available in the given list")


str1 = "sarma"
str2 = "srujan"

str3 = str1 == str2
print(str3)

str4 = str1 > str2
print(str4)

str5 = str1 < str2
print(str5)

str6 = str1 >= str2
print(str6)

str7 = str1 <= str2
print(str7)



num1 = "python \"is\" good"
print(num1)
print('Star\'s Wars')


str8 = str1 != str2
print(str8)





