name = input("Enter your name")

age = float(input('Please Enter a age:\n'))#converting string data type into float datatype and \n is for print the age in next line

print(type(name))

print(type(age))

print("your name is",name,end = "\t",sep = ",")

if age>=12 and age<=20:
    print('and   You are a teenager')
else:
    print('and   You are not a teenager')



print()

print("DATA TYPE CONVERSION")

student_percentage = input("Enter your percentage: ")

print("Your marks prcentage is: ",student_percentage)

print("student percentage type is: ", type(student_percentage))

a = float(student_percentage)

print("After converting from string to float your salary is: ", a)

print("now student percentage type is: ", type(a))
