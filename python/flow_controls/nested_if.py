grade = int(input("please enter your grade:"))
if grade >= 65:
    print("Passing grade of:",grade)

    if grade >= 90:
        if grade > 96:
            print("A+")

        elif 90<=grade<= 96:
            print("A")

        elif grade < 90:
            print("B+")



'''x = int(input('Enter your age: '))

if x > 21:
    if x > 55:
        print("You are too old, you are not eligible for this plan")
    else:
        print("Welcome, you are eligible for this plan")
else:
    print("You are too young, you are not eligible for this plan")'''